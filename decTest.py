from PIL import Image

img_name = "encTest.png"
image = Image.open(img_name)

width, height = image.size

ascii_list = []
text = ""

for x in range(width):
    for y in range(height):
        ascii_list.append(image.getpixel((y, x))[0])

for num in ascii_list:
    text = text + chr(num)

print(text)
