import os
import importlib.util
import shutil
import io
import re
import inspect
from contextlib import redirect_stdout
from colorama import Fore, Style, init
import sys

init(autoreset=True)

class Pytterns:
    def __init__(self, preload=None, loadall=False,break_my_system_security_and_allow_destruction=False):
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            base_dir = sys._MEIPASS
        else:
            base_dir = os.path.dirname(os.path.abspath(__file__))
        
        self.internal_dir = os.path.join(base_dir, "patterns")
        self.user_dir = "patterns"
        if not break_my_system_security_and_allow_destruction:
            self.BANNED_WORDS = [
                "os.", "subprocess", "eval(", "exec(", "open(", 
                 "getattr", "setattr", "__subclasses__", 
                "builtins", "pickle", "socket", "requests", "importlib",
                "threading", "multiprocessing"
            ]
        else:
            self.BANNED_WORDS=[]
        self.color_map = {
            "red": Style.BRIGHT+Fore.RED, "green": Style.BRIGHT+Fore.GREEN, 
            "blue": Style.BRIGHT+Fore.BLUE, "yellow": Style.BRIGHT+Fore.YELLOW, 
            "magenta": Style.BRIGHT+Fore.MAGENTA, "cyan": Style.BRIGHT+Fore.CYAN, 
            "white": Style.BRIGHT+Fore.WHITE, "reset": Fore.RESET
        }
        
        # Cache system (silent)
        self._cache = {}
        self._preload_list = preload or []
        self._loadall = loadall
        
        if self._preload_list:
            self._preload_patterns(self._preload_list)
        elif self._loadall:
            self._load_all_patterns()

    def _get_pattern_path(self, name):
        user_file = os.path.abspath(os.path.join(self.user_dir, f"{name}.py"))
        lib_file = os.path.join(self.internal_dir, f"{name}.py")
        return user_file if os.path.exists(user_file) else lib_file

    def _is_safe(self, file_path):
        
        try:
            with open(file_path, "r", encoding='utf-8') as f:
                content = f.read()
                for word in self.BANNED_WORDS:
                    if word in content: 
                        return False, word
            return True, None
        except: 
            return False, "File Unreadable"

    def _preload_patterns(self, pattern_names):
        for name in pattern_names:
            try:
                file_path = self._get_pattern_path(name)
                if os.path.exists(file_path):
                    safe, reason = self._is_safe(file_path)
                    if safe:
                        spec = importlib.util.spec_from_file_location(name, file_path)
                        module = importlib.util.module_from_spec(spec)
                        spec.loader.exec_module(module)
                        self._cache[name] = module
                    else:
                        self._cache[name] = None  # Silent block
            except:
                self._cache[name] = None  # Silent fail

    def _load_all_patterns(self):
        import glob
        user_patterns = glob.glob(os.path.join(self.user_dir, "*.py"))
        internal_patterns = glob.glob(os.path.join(self.internal_dir, "*.py"))
        
        all_patterns = {}
        for pattern_file in user_patterns + internal_patterns:
            name = os.path.splitext(os.path.basename(pattern_file))[0]
            if name not in all_patterns:
                all_patterns[name] = pattern_file
        
        for name, file_path in all_patterns.items():
            try:
                safe, reason = self._is_safe(file_path)
                if safe:
                    spec = importlib.util.spec_from_file_location(name, file_path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    self._cache[name] = module
                else:
                    self._cache[name] = None
            except:
                self._cache[name] = None

    def _strip_ansi(self, text):
        return re.sub(r'\x1B(?:[@-Z\\-_]|\[[0-9;]*[ -/]*[@-~])', '', text)

    def __getattr__(self, name):
        # Check cache first
        if name in self._cache:
            module = self._cache[name]
        else:
            file_path = self._get_pattern_path(name)
            if not os.path.exists(file_path):
                raise AttributeError(f"Pattern '{name}' not found.")
            
            safe, dangerous_word = self._is_safe(file_path)
            if not safe:
                print(f"SECURITY ALERT: '{name}' contains blocked command: '{dangerous_word}'")
                self._cache[name] = None
                return lambda *args, **kwargs: None
            
            spec = importlib.util.spec_from_file_location(name, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            self._cache[name] = module  # Cache silently

        if module is None:
            return lambda *args, **kwargs: None

        def wrapper(*args, **kwargs):
            center_val = kwargs.get('center', False)
            color_val = kwargs.get('color', None)
            
            if len(args) > 1 and isinstance(args[1], bool):
                center_val = args[1]

            ansi_prefix = self.color_map.get(str(color_val).lower(), "") if color_val else ""

            sig = inspect.signature(module.draw)
            bound_args = sig.bind_partial(*args, **kwargs)
            
            if 'ansi_prefix' in sig.parameters:
                kwargs['ansi_prefix'] = ansi_prefix
            if 'center' in sig.parameters and 'center' not in bound_args.arguments:
                kwargs['center'] = center_val

            f = io.StringIO()
            with redirect_stdout(f):
                try:
                    module.draw(*args, **kwargs)
                except Exception as e:
                    print(f"Error drawing {name}: {e}")

            output = f.getvalue().splitlines()
            term_width = shutil.get_terminal_size().columns

            for line in output:
                formatted = f"{ansi_prefix}{line}{Style.RESET_ALL if ansi_prefix else ''}"
                if center_val:
                    clean_len = len(self._strip_ansi(line))
                    pad = max(0, (term_width - clean_len) // 2)
                    print(" " * pad + formatted, flush=True)
                else:
                    print(formatted, flush=True)
        return wrapper
