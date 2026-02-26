# This is demo code

import time,os
print("Run this code, alongside with the run.py file open, to see how this module works and to understand it better")
time.sleep(5)
os.system("cls" if os.name == "nt" else "clear")


# IN this file, there are all the DEMO for the patterns. You can run this file to see how the patterns work, and how to use them. You can also use this file as a template for your own patterns, by copying the code and modifying it to fit your needs.
# You can use this for your own programs where you need to use precise patterns and don't want to write the code for it yourself. You can also use this as a reference for how to write your own patterns.
# Through this, you dont need to remember code for all the patterns in the world, just remember how to use this library and you can get any pattern you wish.

# If you discover a new pattern, you can add it to the /patterns folder, and it will automatically be available. You can also share your patterns with others by sharing the .py file in the /patterns folder.

# NOTE: To Start, we always use this.
from pytterns import Pytterns
pt = Pytterns()

#To get started, you can get a simple square like this:

pt.square(10)

time.sleep(5)
# Modifying it a bit, you can also center it and change the color like this:
pt.square(10, char="@", center=True, color="cyan")

time.sleep(5)
# For every pattern, we must provide Size. Char is recomended to provide, but it may work without it, depending on the pattern file.

pt.triangle(5, char="#", color="yellow", hollow=False, filler=" ",direction="right",invert=True)

time.sleep(5)
#You can do more cool stuff with mix-matching patterns, like to make loading screens or transitions all in a terminal. Although this may feel a bit laggy, it works, and its quite fun.


#Design1: Upward moving arrows


num=10
colors=["red", "green", "yellow", "blue", "magenta", "cyan"]
while num!=0:
    for i in range(0, 6):
        pt.triangle(i, char="-", color=colors[i], hollow=False, center=True)
        time.sleep(0.05)
    num-=1
        
time.sleep(5)        
#Design2, Square Loading

import os
num=10
colors=["red", "green", "yellow", "blue", "magenta", "cyan"]
while num!=0:
    for i in range(0, 6):
        pt.square(i, char="-", color=colors[i], hollow=False, center=True)
        time.sleep(0.05)
        os.system("cls" if os.name == "nt" else "clear")
    num-=1

time.sleep(5)
# You can also make other shapes, Just check the /patterns folder for the available patterns, and use them in the same way as shown above..
# You can also mix and match patterns to create more complex designs.

# The possibilities are endless!
