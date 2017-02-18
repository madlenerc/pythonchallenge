from PIL import Image

with Image.open('../data/oxygen.png', 'r') as img:
    width = img.width
    height = img.height

    line = int(height / 2)
    pixel_width = 7

    bytes = []
    for i in range(0, width, pixel_width):
        bytes.append(img.getpixel((i, line))[0])

print(''.join(chr(int(b)) for b in bytes))
print(''.join(chr(int(b)) for b in [105, 110, 116, 101, 103, 114, 105, 116, 121]))