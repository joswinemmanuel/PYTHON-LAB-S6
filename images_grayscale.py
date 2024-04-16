from  images import Image

def gray_scale(im):
    for x in range(im.getWidth()):
        for y in range(im.getHeight()):
            r, g, b = im.getPixel(x, y)
            r = int(r * .299)
            g = int(g * .587)
            b = int(b * .114)
            lem = r + g + b
            im.setPixel(x, y, (lem, lem, lem))
    im.draw()

im = Image("jesus.gif")
gray_scale(im)
