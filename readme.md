# Pytterns
### One stop library for all your Terminal Patterns

With pytterns, you can make your projects pop with patterns and shapes. With this, you can print any pattern, with high customization, in any senario in the terminal. You can even make your custom Patterns through .py based pattern template system. This project has solid security and large compatibility with terminal sizes, color rendering, and OS. If you are working on a terminal project, need a loading page or you need to print shapes in any case, No need to learn each and every pattern. Just use Pytterns!

## How it works
Pytterns has default patterns which can be used to get basic shapes with quite a lot of customization directly printed in the console.

You may also make your own pattern theme by making your own .py templates. Once added to Pytterns, you can use it in your code RIGHT AWAY!

## Installation

To get started, you can use 2 options.

1. Download the files from git and integrate with your code.

OR

2. Download the library through pip. → [Download Through PIP](https://pypi.org/project/get-pytterns/0.1.0/)

## Get started with Default Pytterns
Each Pyttern Pattern file which is made by me is heavily documented, so if you open it in the /patterns folder, you can get a good understanding of the args and how its processed.

Once installed, just use this to start using Pytterns in your code

```py
from pytterns import Pytterns
pt = Pytterns()
```

## Basic Default Args for Patterns

To make any supported shape, we use the following method to print it in the terminal:

```
pt.<shape name>(<size>, char=<char>, center=<Bool>, color=<color> ...)
```

For a simple square of side length 10:
```py
pt.square(10)
```

Output:
```
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
```

# Char
To make this same square with different characters, we can use the char arg.

Char takes in a String Input.

For Example, to make the above square with "x":

```py
pt.square(10,char="x")
```
*You get a square made with x*

# Center
With the center arg, we can center most of the shapes perfectly in the terminal.

Center takes a boolean input, True/False 

For Example, to center the above square, we use:

```py
pt.square(10, char="x", center=True)
```

# Color
With the color arg, you can color your shapes with the following colors:

- red
- green
- blue
- yellow
- magenta
- cyan
- white
- reset

For example, you can color the above square like:
```py
pt.square(10, char="x", center=True,color="red")
```


# Hollow
With the hollow arg, you can make shapes hollow, and just get its border.

The hollow arg takes in a Boolean, True/False.

For Example, you can make a **Red** **Centered** **hollow** square of **radius 10**, made with **$** like:

```py
pt.square(10, char="$",center=True,color="red",hollow=True)
```
Output:

```diff
-$ $ $ $ $ $ $ $ $ $
-$                 $
-$                 $
-$                 $
-$                 $
-$                 $
-$                 $
-$                 $
-$                 $
-$ $ $ $ $ $ $ $ $ $
```
*Terminal render would be proper and centered.*

# Filler

As you may have noticed in above output examples, each shape has a space (filler) between the characters. This is a space by default, but we can customize this through the filler arg.

For Example, for the above hollow square filled with Spaces, we can make it fill with - through:

```py
pt.square(10, char="$",center=True,color="red",hollow=True, filler="-")
```

Output:
```diff
- $-$-$-$-$-$-$-$-$-$
- $-----------------$
- $-----------------$
- $-----------------$
- $-----------------$
- $-----------------$
- $-----------------$
- $-----------------$
- $-----------------$
- $-$-$-$-$-$-$-$-$-$
```
*Terminal render would be proper and centered.*

# Other Important Args

For special shapes like Triangles or Pyramids, which could be flipped upside down, Direction and Invert can be used.

### Direction:
Used to set pointing direction of a supported shape.

For Example, We can make a triangle point to 2 directions, Left and Right:

```py
pt.triangle(10, char="*",hollow=True,filler="-",direction="left")
```

Output:
```
*-
*-*-
*- -*-
*- - -*-
*- - - -*-
*- - - - -*-
*- - - - - -*-
*- - - - - - -*-
*- - - - - - - -*-
*-*-*-*-*-*-*-*-*-*-
```

### Invert:

With this, we can make supported shapes Upside-Down. This can be used with direction arg to gain full control of the shape's pointing.

For example, to make a left triangle inverted we use:

```py
pt.triangle(10, char="*",hollow=True,filler="-",direction="left",invert=True)
```

Output:
```
*-*-*-*-*-*-*-*-*-*-
*- - - - - - - -*-
*- - - - - - -*-
*- - - - - -*-
*- - - - -*-
*- - - -*-
*- - -*-
*- -*-
*-*-
*-
```

# Custom Templates
Through templates, we can make custom patterns based on our own code, and seamlessly use it just like we did with the default code.

This may sound difficult, but we don't even need a bit of advanced programming for this.

### Getting Started:
Firstly ensure Pytterns is installed in your project. Then make a folder ``/patterns`` in your project's root directory.

You can create files in this folder now, and through this you can add custom patterns to your projects.

Once you make a .py file, start with the ``draw()`` function and define the args you need for the pattern you are trying to make. *Size and Center is always must to keep, rest args are based on your wish.*

For Example, this is the function definition for Triangles.
```py
def draw(size,center, char="*", filler=" ", hollow=False, direction="left", invert=False):
```
In this, Size (int) is the shape's size, and Center is a boolean telling if trigger has opted for centering or not.

⭐**Note: If you wish to use centering in your code, you need not to make any centering system in your template file. Just make sure its compatible with our centering and you are good to go. Similarly, you also do not need to worry about colors, those get added automatically too!**

After this, you can just make your pattern function, and print the output in that function itself and the Pytterns takes care of everything!

# Advanced Use
With pytterns, you can also make terminal animations/loading-graphics.

For Example, if you want fast upward moving arrows, use this:

```py
import time
colors=["red", "green", "yellow", "blue", "magenta", "cyan"]

while True:
    for i in range(0, 6):
        pt.triangle(i, char="-", color=colors[i], hollow=False, center=True)
        time.sleep(0.05)
    
```
Output:

![Upward Moving Arrows](https://i.ibb.co/Y451nNXb/image.png)

*It would be animated due to loop, demo videos in /media folder



Or, For Example you can use my favorite, the Square Loading:
```py
import time,os
colors=["red", "green", "yellow", "blue", "magenta", "cyan"]
while True:
    for i in range(0, 6):
        pt.square(i, char="-", color=colors[i], hollow=False, center=True)
        time.sleep(0.05)
        os.system("cls" if os.name == "nt" else "clear")
```
For this you would need to see the video at /media folder


# Contribution

This project is all open for your contributions! You can make more patterns for the default installation, and fix common rendering bugs.
Lets together make the best python patterns library in the world!

# License
MIT
