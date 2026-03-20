# This writes text in python, like a out.write statement, but with delays and emotions!

import sys
import time
import re
import shutil

def draw(content, center, mode="letter", delay=0.05, end="\n",
         splitter=" ",reset_end=True, **kwargs):
    
    out = sys.__stdout__
    term_width = shutil.get_terminal_size().columns
    
    colors = {
        '\\red': '\033[91m', '\\green': '\033[92m', '\\blue': '\033[94m',
        '\\yellow': '\033[93m', '\\magenta': '\033[95m', '\\cyan': '\033[96m', '\\white': '\033[0m',
        "\\reset": "\033[0m"
    }
        
    # --- FIX STARTS HERE ---
    # Calculate the total length of all strings combined before starting the loop
    if center:
        total_len = sum(len(str(item)) for item in content if isinstance(item, str) and item not in colors)
        padding = (term_width - total_len) // 2
        out.write(" " * padding)
    # --- FIX ENDS HERE ---
    
    for i in content:
        
        if isinstance(i, (int, float)):
            time.sleep(i)
            continue
        
        elif i in colors:
            out.write(colors[i])
            out.flush()
            continue
        
        else:
            # Removed the 'if center' from here to prevent doubling
            if mode == "word":
                words = i.split(splitter)
                for idx, w in enumerate(words):
                    out.write(w)
                    if idx < len(words) - 1:
                        out.write(splitter)
                    out.flush()
                    time.sleep(delay)
                    
            elif mode == "letter":
                for j in i:
                    out.write(j)
                    out.flush()
                    time.sleep(delay)
            else:
                out.write(i)
                out.flush()
                time.sleep(delay)

    if reset_end:
        out.write("\033[0m" + end)
    else:
        out.write(end)
    out.flush()