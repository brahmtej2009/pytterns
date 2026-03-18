import numpy as np
import time
import shutil
import sys

def draw(char="█", size=100, rot_speed=5,refresh_time=0.03, rotate=False, duration=None, angle=0.0, colored=True,clr_screen=True, **kwargs):
    # Bypass the framework's buffer to allow real-time animation
    real_out = sys.__stdout__
    
    size=size/100
    rot_speed=rot_speed/100
    C = {
        'r': '\033[91m', 'g': '\033[92m', 'b': '\033[94m',
        'y': '\033[93m', 'm': '\033[95m', 'c': '\033[96m', 'w': '\033[0m'
    }

    v_base = np.array([
        [-1,-1,-1], [1,-1,-1], [1,1,-1], [-1,1,-1],
        [-1,-1,1], [1,-1,1], [1,1,1], [-1,1,1]
    ]) * float(size)

    edges = [
        (0,1,'r'), (1,2,'r'), (2,3,'r'), (3,0,'r'),
        (4,5,'g'), (5,6,'g'), (6,7,'g'), (7,4,'g'),
        (0,4,'b'), (1,5,'y'), (2,6,'m'), (3,7,'c')
    ]

    curr_a = float(angle)
    t_start = time.time()
    
    # Hide cursor for cleaner look
    real_out.write("\033[?25l")

    try:
        while True:
            if duration and (time.time() - t_start > duration):
                break

            term = shutil.get_terminal_size()
            cols, rows = term.columns, term.lines
            cx, cy = cols // 2, rows // 2

            ca, sa = np.cos(curr_a), np.sin(curr_a)
            ca2, sa2 = np.cos(curr_a * 0.7), np.sin(curr_a * 0.7)
            
            rx = np.array([[1,0,0], [0,ca,-sa], [0,sa,ca]])
            ry = np.array([[ca2,0,sa2], [0,1,0], [-sa2,0,ca2]])
            
            rv = v_base @ rx @ ry
            
            scr = []
            for v in rv:
                # Vertical stretch (rows/4) vs Horizontal (cols/6) to keep cube square
                scr.append((int(v[0] * (cols/6) + cx), int(v[1] * (rows/4) + cy)))

            buf = [[' ' for _ in range(cols)] for _ in range(rows)]
            
            for n1, n2, ck in edges:
                p1, p2 = scr[n1], scr[n2]
                for t in np.linspace(0, 1, 16):
                    lx = int(p1[0] + (p2[0] - p1[0]) * t)
                    ly = int(p1[1] + (p2[1] - p1[1]) * t)
                    if 0 <= lx < cols and 0 <= ly < rows:
                        buf[ly][lx] = f"{C[ck]}{char}{C['w']}" if colored else char

            # Direct write to the real terminal handle
            # \033[H moves cursor to top; \033[J clears old pixels
            
            cursor_funcs="\033[H"
            if clr_screen:
                cursor_funcs="\033[2J\033[H"
                
            real_out.write(cursor_funcs + "\n".join("".join(r) for r in buf))
            real_out.flush()

            if not rotate:
                break
                
            curr_a += rot_speed
            
            time.sleep(refresh_time)
    finally:
        # Show cursor again on exit
        real_out.write("\033[?25h")
        real_out.flush()