# This file takes in all the patterns from the /patterns folder, and makes functions out of it.
# For example, if you put a pattern file in the /patterns folder called "square.py", you can then use pytterns.py.square(<args>) to trigger the pattern.
# Its really simple to add more patterns and features to this.. to do that, just add a new .py file in the /patterns folder.Write your entire pattern in a draw() function that takes in the size and center and other optional args as u wish and make anything you want after that.


#NOTE: This file is having some AI generated code due to complexity and security concerns so if someone tries to use it for production, it doesnt cause boom booms from malicious scripts.
# The code is designed to be secure by scanning the pattern files for potentially dangerous commands before executing them. If a pattern file contains any of the banned words, it will not be executed and a security alert will be printed instead. This helps to prevent malicious code from being run through the patterns library.
# This approach is kinda basic, and I'm open to suggestions for improving the security of the library. The current implementation is a simple keyword scan, which may not catch all malicious code, but it provides a basic level of protection against common dangerous commands.

import os
import importlib.util
import shutil
import io
import sys
from contextlib import redirect_stdout
from colorama import Fore, Style, init

init(autoreset=True)

class Pytterns:
    def __init__(self):
        # This part ensures the library finds its own built-in patterns after pip install
        self.internal_dir = os.path.join(os.path.dirname(__file__), "patterns")
        # This looks for a 'patterns' folder in the user's current project
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

    def _is_safe(self, file_path): # AI Generated for security
        with open(file_path, "r") as f:
            content = f.read()
            for word in self.BANNED_WORDS:
                if word in content: return False, word
        return True, None

    def __getattr__(self, name):
        # We check the local folder first, then the library's internal folder
        user_file = os.path.join(self.user_dir, f"{name}.py")
        lib_file = os.path.join(self.internal_dir, f"{name}.py")

        if os.path.exists(user_file):
            file_path = user_file
        elif os.path.exists(lib_file):
            file_path = lib_file
        else:
            raise AttributeError(f"Pattern '{name}' not found.")

        safe, dangerous_word = self._is_safe(file_path)
        if not safe:
            print(f"SECURITY ALERT: '{name}' contains blocked command: '{dangerous_word}'")
            return lambda *args, **kwargs: None

        spec = importlib.util.spec_from_file_location(name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        def wrapper(*args, center=False, color=None, **kwargs): #This is the AI Part
            f = io.StringIO()
            with redirect_stdout(f):
                try:
                    # Pass center to the draw function so it knows to skip manual padding
                    module.draw(*args, center=center, **kwargs)
                except Exception as e:
                    print(f"Error drawing {name}: {e}")
            
            output = f.getvalue().splitlines() 
            ansi_color = self.color_map.get(str(color).lower(), "") if color else ""
            
            for line in output:
                # Strip leading/trailing spaces if centering to avoid double-offset
                if center == True:
                    clean_line = line.strip()
                else:
                    clean_line = line
                
                formatted_line = ansi_color + clean_line
                
                if center:
                    # Adjust centering width for the length of hidden ANSI color codes
                    actual_width = self.width + len(ansi_color)
                    print(formatted_line.center(actual_width), flush=True)
                else:
                    print(formatted_line, flush=True)
        
        return wrapper