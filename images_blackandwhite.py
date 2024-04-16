from images import Image

def black_and_white(im):
    black = (0, 0, 0)
    white = (255, 255, 255)
    for x in range(im.getWidth()):
        for y in range(im.getHeight()):
            r, g, b = im.getPixel(x, y)
            avg = (r+g+b) // 3
            if avg > 128:
                im.setPixel(x, y, white)
            else:
                im.setPixel(x, y, black)
    im.draw()

im = Image("jesus.gif")
black_and_white(im)
