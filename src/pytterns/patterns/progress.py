import re
from colorama import Fore, Style

def _strip_ansi(text):
    return re.sub(r'\x1B(?:[@-Z\\-_]|\[[0-9;]*[ -/]*[@-~])', '', text)

def draw(size, *args, center=False, progress=50, 
         ansi_prefix="", fill="█", blank="░", 
         fill_color="yellow", blank_color="black",end="\n", **kwargs):

    progress = progress / 100  # Convert % to 0-1
    content = args[0] if args else [""]
    
    # Colorama color mapping
    fill_colors = {
        "green": Fore.GREEN, "red": Fore.RED, "yellow": Fore.YELLOW,
        "blue": Fore.BLUE, "cyan": Fore.CYAN, "magenta": Fore.MAGENTA,
        "white": Fore.WHITE, "grey": Fore.LIGHTBLACK_EX
    }
    blank_colors = {**fill_colors, "grey": Fore.LIGHTBLACK_EX, "dark": Fore.BLACK}
    
    # Since we cant use the get-attr due to security protocol, we are using this method.
    fill_color_code = fill_colors.get(fill_color.lower(), Fore.GREEN)
    blank_color_code = blank_colors.get(blank_color.lower(), Fore.LIGHTBLACK_EX)
    
    # Build colored bar
    filled_len = int(progress * (size - 2))  # -2 for borders
    bar = (fill_color_code + fill * filled_len + 
           Style.RESET_ALL + blank_color_code + blank * (size - 2 - filled_len) + Style.RESET_ALL)
    
    # Add percentage text 
    pct = f"{progress*100:.0f}%"
    final_line = f"[ {bar.ljust(size-4)} ] {pct}"
    
    print(f"{ansi_prefix}{final_line}",end=end)
