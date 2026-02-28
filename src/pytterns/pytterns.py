import os
import importlib.util
import shutil
import io
import re
from contextlib import redirect_stdout
from colorama import Fore, Style, init

init(autoreset=True)

class Pytterns:
    def __init__(self):
        self.internal_dir = os.path.join(os.path.dirname(__file__), "patterns")
        self.user_dir = "patterns"
        self.width = shutil.get_terminal_size().columns
        self.BANNED_WORDS = [
            "os.", "subprocess", "eval(", "exec(", "open(", 
            "shutil", "getattr", "setattr", "__subclasses__", 
            "builtins", "pickle", "socket", "requests", "importlib",
            "sys.", "threading", "multiprocessing"
        ]
        self.color_map = {
            "red": Style.BRIGHT+Fore.RED, "green": Style.BRIGHT+Fore.GREEN, "blue": Style.BRIGHT+Fore.BLUE,
            "yellow": Style.BRIGHT+Fore.YELLOW, "magenta": Style.BRIGHT+Fore.MAGENTA, 
            "cyan": Style.BRIGHT+Fore.CYAN, "white": Style.BRIGHT+Fore.WHITE, "reset": Fore.RESET
        }

    def _is_safe(self, file_path):
        with open(file_path, "r", encoding='utf-8') as f:
            content = f.read()
            for word in self.BANNED_WORDS:
                if word in content: return False, word
        return True, None

    def _strip_ansi(self, text):
        return re.sub(r'\x1B(?:[@-Z\\-_]|\[[0-9;]*[ -/]*[@-~])', '', text)

    def __getattr__(self, name):
        user_file = os.path.join(self.user_dir, f"{name}.py")
        lib_file = os.path.join(self.internal_dir, f"{name}.py")

        if os.path.exists(user_file): file_path = user_file
        elif os.path.exists(lib_file): file_path = lib_file
        else: raise AttributeError(f"Pattern '{name}' not found.")

        safe, dangerous_word = self._is_safe(file_path)
        if not safe:
            print(f"SECURITY ALERT: '{name}' contains blocked command: '{dangerous_word}'")
            return lambda *args, **kwargs: None

        spec = importlib.util.spec_from_file_location(name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        def wrapper(*args, center=False, color=None, **kwargs):
            # Calculate prefix here to pass it into the draw function
            ansi_prefix = self.color_map.get(str(color).lower(), "") if color else ""
            
            f = io.StringIO()
            with redirect_stdout(f):
                try:
                    # Added ansi_prefix to kwargs so pattern can fix right-side border color
                    module.draw(*args, center=center, ansi_prefix=ansi_prefix, color=color, **kwargs)
                except Exception as e:
                    print(f"Error drawing {name}: {e}")
            
            output = f.getvalue().splitlines() 
            for line in output:
                # Apply the global color prefix to the whole line
                formatted_line = ansi_prefix + line
                
                if center:
                    real_width = len(self._strip_ansi(line))
                    padding = (self.width - real_width) // 2
                    print(" " * max(0, padding) + formatted_line, flush=True)
                else:
                    print(formatted_line, flush=True)
        
        return wrapper