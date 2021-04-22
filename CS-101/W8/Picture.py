from PIL import Image

background_image = Image.open('/Users/smelcerc/Code/GitHub/smelcerc.github.io/CS-101/W8/cse110_images/snowscape.jpg')
forground_image = Image.open('/Users/smelcerc/Code/GitHub/smelcerc.github.io/CS-101/W8/cse110_images/penguin.jpg')
sunset_image = Image.open('/Users/smelcerc/Code/GitHub/smelcerc.github.io/CS-101/W8/cse110_images/sunset.jpg')

bg_width, bg_height = background_image.size
fg_width, fg_height = forground_image.size

pixels_original_ss = sunset_image.load()
pixels_original_bg = background_image.load()
pixels_original_fg = forground_image.load()

for h in range(bg_height):
    for w in range(bg_width):
        if h <= 175:
            r, g, b = pixels_original_ss[w, h]
            pixels_original_bg[w, h] = (r, g, b)

for h in range(fg_height):
    for w in range(fg_width):
        r, g, b = pixels_original_fg[w, h]
        if r <= 90 and g >= 175 and b <= 110:
            pixels_original_fg[w, h] = (255, 0, 93)
        else:
            pixels_original_bg[w, h] = (r, g, b)
        
background_image.save('/Users/smelcerc/Code/GitHub/smelcerc.github.io/CS-101/W8/cse110_images/snowscapeSunset.jpg')