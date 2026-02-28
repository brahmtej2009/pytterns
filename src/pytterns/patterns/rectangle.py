# Default - Rectangle

# This rectangle is measured by number of characters, so due to the 2:1 Char ratio, you need to input correct size to get the desired rectangle. 

def draw(length, width, center, char="*", filler=" ", hollow=False):

    size = length if length > width else width

    for row in range(size):
        

        if hollow == False:
            line = ""
            for col in range(size):
                if col == size - 1:
                    line = line + char
                else:
                    line = line + char + filler
            print(line)
            
        else:
            
            if row == 0 or row == size - 1:
                line = ""
                for col in range(size):
                    if col == size - 1:
                        line = line + char
                    else:
                        line = line + char + filler
                print(line)
            
            
            else:
                line = char
                
                
                full_row_len = len((char + filler) * (size - 1) + char)
                middle_section = filler * (full_row_len - (len(char) * 2))
                
                print(char + middle_section + char)