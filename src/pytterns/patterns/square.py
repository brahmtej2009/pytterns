# Square pattern -- DEFAULT

# Size is the length of the side of square, Char is the character to use for the square, and Filler is the character to use for the space between the characters.
# By default, the Char is "*" and the Filler is " ", but you can change them to whatever you like through args.
# You can also add more arguments to the pattern, but that depends on how you want to customize it.

# Have ideas? Instead of editing this file locally, Submit your idea on github and I might add it to the library for public use!
# You may also make a new file in this folder, and add your own pattern there, just make sure to follow the same structure as this file, and have a draw() function with arguments you want for processing.


#NOTE: This works better for smaller numbers, but breaks for bigger ones due to terminal text ratio. For a bigger square, use the reg_square pattern.


def draw(size, center, char="*", filler=" ", hollow=False):

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