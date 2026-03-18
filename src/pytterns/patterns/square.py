def draw(size, *args, center=False, char="*", filler=" ", hollow=False, ansi_prefix="", **kwargs):
    for row in range(size):
        if not hollow:
            # Full square
            line = ""
            for col in range(size):
                line += char + filler
            line = line.rstrip(filler)  # Remove trailing filler
            print(f"{ansi_prefix}{line}")
        else:
            # Hollow square - PERFECT EDGES
            if row == 0 or row == size - 1:
                # Top/Bottom: FULL border with $...$
                line = ""
                for col in range(size):
                    line += char + filler
                line = line.rstrip(filler)
                print(f"{ansi_prefix}{line}")
            else:
                # Middle: $ + filler + $
                left_edge = char
                right_edge = char
                middle_fillers = filler * ((size * 2 - 3))  # Exact match length
                line = left_edge + middle_fillers + right_edge
                print(f"{ansi_prefix}{line}")
