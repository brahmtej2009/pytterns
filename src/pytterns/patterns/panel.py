import re,sys
from colorama import Style

def _strip_ansi(text):
    return re.sub(r'\x1B(?:[@-Z\\-_]|\[[0-9;]*[ -/]*[@-~])', '', text)

def draw(size,content,center, title=None, padding=1, 
         v_border=None, h_border=None, 
         top_left=None, top_right=None, bottom_left=None, bottom_right=None,
         border_bold=False, center_content=True, 
         ansi_prefix="", **kwargs):

    # This is the border's char, this specific is used as it uses the full height/width of ascii block and merges properly
    v, h = ("┃", "━") if border_bold else ("│", "─")
    tl, tr = ("┏", "┓") if border_bold else ("┌", "┐")
    bl, br = ("┗", "┛") if border_bold else ("└", "┘")

    
    v, h = v_border or v, h_border or h
    tl, tr = top_left or tl, top_right or tr
    bl, br = bottom_left or bl, bottom_right or br

    # Default padding and user defined padding
    inner_width = size - 2
    content_width = inner_width - (2 * padding)


    if title:
        title_stripped = _strip_ansi(str(title))  # Title with color codes fixed
        title_display_len = len(title_stripped) + 2  # Some more padding
        bar_len = inner_width - title_display_len
        l_bar = h * (bar_len // 2)
        r_bar = h * (bar_len - len(l_bar))
        l1=f"{ansi_prefix}{tl}{l_bar}{Style.RESET_ALL} {title} {ansi_prefix}{r_bar}{tr}\n" # Rendered line 1, with title

    else:
        l1=f"{ansi_prefix}{tl}{h * inner_width}{tr}\n" # IF no title, straight line

  
    l2=""
    pad_str = " " * padding
    
    # Each element in list is a new line, and it gets rendered here in a multiline string
    for line in content:
        real_len = len(_strip_ansi(line))
        diff = content_width - real_len
        
        if center_content:
            l_space = " " * (diff // 2)
            r_space = " " * (diff - len(l_space))
            formatted = f"{l_space}{line}{r_space}"
        else:
            formatted = f"{line}{' ' * diff}"
        
        
        l2+=f"{ansi_prefix}{v}{Style.RESET_ALL}{pad_str}{formatted}{Style.RESET_ALL}{ansi_prefix}{pad_str}{v}\n" # Rendered multiline string with right colors and borders

    # Add the last row on the bottom of the panel to complete the border
    l3=f"{ansi_prefix}{bl}{h * inner_width}{br}"
    
    sys.stdout.write(l1+l2+l3) # Sum write flush
    sys.stdout.flush()