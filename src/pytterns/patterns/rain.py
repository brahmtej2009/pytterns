import random
import time
import shutil
import sys
from colorama import Fore, Style

def draw(size, center, duration=5, chars="X01@#$%&*", 
         delay=0.04, color="green", glitch_chance=10, 
         glitch_color="white", prefix="", bold=True, 
         width_override=None, density=100):
    
    glitch_chance=glitch_chance/100
    density=density/100
    color_map = {
        "red": Fore.RED, "green": Fore.GREEN, "blue": Fore.BLUE,
        "yellow": Fore.YELLOW, "magenta": Fore.MAGENTA, 
        "cyan": Fore.CYAN, "white": Fore.WHITE
    }
    
    base_color = color_map.get(color.lower(), Fore.GREEN)
    g_color = color_map.get(glitch_color.lower(), Fore.WHITE)
    style_mod = Style.BRIGHT if bold else Style.NORMAL
    

    term_cols = shutil.get_terminal_size().columns
    actual_size = size if size is not None else 0
    

    total_target_width = width_override if width_override else (actual_size if (center and actual_size > 0) else term_cols)
    
    char_space = max(0, total_target_width - len(prefix))
        
    start_time = time.time()
    lines_printed = 0

    try:
        while True:
            if duration is not None and (time.time() - start_time) > duration:
                break
            if actual_size > 0 and lines_printed >= actual_size and not duration:
                break

            line_chars = ""
            for _ in range(char_space):
                if random.random() > density:
                    line_chars += " "
                    continue
                
                char = random.choice(chars)
                if random.random() < glitch_chance:
                    line_chars += f"{g_color}{char}{base_color}{style_mod}"
                else:
                    line_chars += char


            final_line = f"{base_color}{style_mod}{prefix}{line_chars}"
            
            if center:
                padding = max(0, (term_cols - total_target_width) // 2)
                output = (" " * padding) + final_line + "\n"
            else:
                output = final_line + "\n"

# We use sys for writing because pytterns has its own buffer for the print stuff, which causes issues with
# features that should be printed live
            sys.__stdout__.write(output)
            sys.__stdout__.flush()

            lines_printed += 1
            time.sleep(delay)

    except KeyboardInterrupt:
        sys.__stdout__.write(Style.RESET_ALL + "\n")
        sys.__stdout__.flush()