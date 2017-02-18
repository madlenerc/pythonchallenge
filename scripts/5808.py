# level 11
from PIL import ImageDraw, Image

with Image.open('../data/cave.jpg') as original:
    orig_width, orig_height = original.size
    new_width = int(orig_width/2)
    new_height = int(orig_height / 2)

    with Image.new(original.mode, (new_width, new_height)) as new:
        draw = ImageDraw.Draw(new)

        for x in range(new_width):
            for y in range(new_height):
                # keep odd pixels in even rows
                orig_position = (2 * x + y % 2, y)
                pixel = original.getpixel(orig_position)
                draw.point((x, y), pixel)

        new.show()
