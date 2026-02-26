# Currently this does not work with Centered, and just displays a Pyramid.
# Looking for improvements in this.


def draw(size,center, char="*", filler=" ", hollow=False, direction="left", invert=False):

# In this we basically take direction, left or right, and based on that we make a right angled triangle. Then to make its origion on top, we use invert.
# Through this we can make all 4 types of right angled triangles.


    if direction == "left":
        if invert == False:
            for i in range(1, size + 1):
                for j in range(1, i + 1):
                    if hollow == True:
                        if j == 1 or j == i or i == size:
                            print(char, end=filler)
                        else:
                            # manually printing spaces for hollow center
                            print(" ", end=filler)
                    else:
                        print(char, end=filler)
                print()
        else:
            for i in range(size, 0, -1):
                for j in range(1, i + 1):
                    if hollow == True:
                        if j == 1 or j == i or i == size:
                            print(char, end=filler)
                        else:
                            print(" ", end=filler)
                    else:
                        print(char, end=filler)
                print()

    elif direction == "right":
        if invert == False:
            for i in range(1, size + 1):
                # printing leading spaces one by one
                for s in range(size - i):
                    print(" ", end=" ")
                for j in range(1, i + 1):
                    if hollow == True:
                        if j == 1 or j == i or i == size:
                            print(char, end=filler)
                        else:
                            print(" ", end=filler)
                    else:
                        print(char, end=filler)
                print()
        else:
            for i in range(size, 0, -1):
                # printing leading spaces for inverted right triangle
                for s in range(size - i):
                    print(" ", end=" ")
                for j in range(1, i + 1):
                    if hollow == True:
                        if j == 1 or j == i or i == size:
                            print(char, end=filler)
                        else:
                            print(" ", end=filler)
                    else:
                        print(char, end=filler)
                print()