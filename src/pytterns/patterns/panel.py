import re
from colorama import Style

def _strip_ansi(text):
    return re.sub(r'\x1B(?:[@-Z\\-_]|\[[0-9;]*[ -/]*[@-~])', '', text)

def draw(size, center, content, title=None, padding=1, 
         v_border=None, h_border=None, 
         top_left=None, top_right=None, bottom_left=None, bottom_right=None,
         border_bold=False, center_content=True, 
         ansi_prefix="", **kwargs):

    # 1. Defaults & Bold Logic (Using the chars you liked)
    v, h = ("┃", "━") if border_bold else ("│", "─")
    tl, tr = ("┏", "┓") if border_bold else ("┌", "┐")
    bl, br = ("┗", "┛") if border_bold else ("└", "┘")

    # 2. Manual Overrides (Highest priority)
    v, h = v_border or v, h_border or h
    tl, tr = top_left or tl, top_right or tr
    bl, br = bottom_left or bl, bottom_right or br

    # 3. Geometry
    inner_width = size - 2
    content_width = inner_width - (2 * padding)

    # 4. Header
    if title:
        title_str = f" {title} "
        bar_len = inner_width - len(title_str)
        l_bar = h * (bar_len // 2)
        r_bar = h * (bar_len - len(l_bar))
        # Sandwich: [Color]Border+Bar [Reset]Title [Color]Bar+Border
        print(f"{ansi_prefix}{tl}{l_bar}{Style.RESET_ALL}{title_str}{ansi_prefix}{r_bar}{tr}")
    else:
        print(f"{ansi_prefix}{tl}{h * inner_width}{tr}")

    # 5. Content
    pad_str = " " * padding
    for line in content:
        real_len = len(_strip_ansi(line))
        diff = content_width - real_len
        
        if center_content:
            l_space = " " * (diff // 2)
            r_space = " " * (diff - len(l_space))
            formatted = f"{l_space}{line}{r_space}"
        else:
            formatted = f"{line}{' ' * diff}"
        
        # Perfect Vertical Alignment: [Color]V [Reset]Pad+Text [Color]Pad+V
        print(f"{ansi_prefix}{v}{Style.RESET_ALL}{pad_str}{formatted}{Style.RESET_ALL}{ansi_prefix}{pad_str}{v}")

    # 6. Footer
    print(f"{ansi_prefix}{bl}{h * inner_width}{br}")