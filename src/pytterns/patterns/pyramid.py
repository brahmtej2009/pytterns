# For pyramid, we take a different approach. This is because when the pyramid is not centered, our normal code can work.
# But when the pyramid is centered, the space characters on one side of the pyramid can cause centering issues and the pattern can get messed up.

# To fix this, we can detect if the pyramid is centered, and if it is, we can just start with 1 Char and increase its number as we go down, and center system would center it by itself.


# 


#NOTE: Learnt this from https://www.geeksforgeeks.org/python/programs-printing-pyramid-patterns-python/



def draw(size,center, char="#",filler=" ", hollow=False,invert=False):
    print(center)
    if hollow:
        for i in range(1, size + 1):
            for j in range(1, 2 * size):
                if j == size - i + 1 or j == size + i - 1 or i == size:
                    print(char, end="")
                else:
                    print(filler, end="")
            print()
    if hollow == False:
        for i in range(1, size + 1):
            # Print leading spaces
            for j in range(size - i):
                print(filler, end="")
            
            # Print asterisks for the current row
            for k in range(1, 2*i):
                print(char, end="")
            print()
   
