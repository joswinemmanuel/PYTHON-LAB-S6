from images import Image

im = Image(1000, 500)
y = im.getHeight() // 2
blue = (0, 0, 255)

for x in range(im.getWidth()):
    im.setPixel(x, y+1, blue)
    im.setPixel(x, y, blue)
    im.setPixel(x, y+1, blue)

im.draw()
