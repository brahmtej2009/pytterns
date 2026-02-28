# This is a special pattern function. Usually, due to terminal fonts having a 2:1 ratio in height and width, we can not make a proper regular square if we measure in side distance.
# Although we can make a square by measuring in character distance, it would look more like a rectangle due the ratio thingy.
# This Regular Square pattern is designed so it gives a square whose sides are same in length, but number of char in vertical/horizontal may vary to make it possible.

# This may break for small numbers, but works better for bigger numbers.

 #NOTE: I Used AI for this because making a regular square pattern is a bit more complex than the other patterns, and I wanted to make sure it looks good and works well. The AI helped me to come up with a design that takes into account the aspect ratio of the terminal characters, and creates a square that looks more like a square than a rectangle.
# I also made sure sure it has the same customization options as the other patterns, such as hollow and filler etc.
   
def draw(size, center, char="#", filler=" ", hollow=False):
    line_str = ""
    for i in range(size):
        if i == size - 1:
            line_str = line_str + char
        else:
            line_str = line_str + char + filler
    
    total_w = len(line_str)
    
    # 2.3 is the ratio to make it look like a real square [This was processed through AI]
    h_calc = total_w / 2.3
    height = int(h_calc + 0.5) 
    
    if height < 1:
        height = 1

    for r in range(height):
        if hollow == True:
            if r == 0 or r == height - 1:
                print(line_str)
            else:
                # build the gap for the middle [Logic from AI]
                side_w = len(char)
                spaces = total_w - (side_w * 2)
                
                gap = ""
                for s in range(spaces):
                    gap = gap + filler
                
                print(char + gap + char)
        else:
            print(line_str)