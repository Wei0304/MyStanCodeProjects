"""
File: blur.py
Name:
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: A image file (can be png. jpg. etc), original image
    :return new_img: blurred image
    Function: Can blur the imported original image
    """

    new_img = SimpleImage.blank(img.width, img.height)
    for y in range(img.height):
        for x in range(img.width):

            pixel = new_img.get_pixel(x, y)

            total_red = 0
            total_green = 0
            total_blue = 0
            num = 0

            if x == 0:  # lower bound of x
                r_low = x
            else:
                r_low = x - 1
            if x == (img.width-1):  # upper bound of x
                r_upp = x
            else:
                r_upp = x + 1
            if y == 0:    # upper bound of y
                c_upp = y
            else:
                c_upp = y - 1
            if y == (img.height-1):  # lower bound of y
                c_low = y
            else:
                c_low = y + 1

            for r in range(r_low, r_upp+1):    # Calculate the total RGB value separately
                for c in range(c_upp, c_low+1):
                    total_red += img.get_pixel(r, c).red
                    total_blue += img.get_pixel(r, c).blue
                    total_green += img.get_pixel(r, c).green
                    num += 1

            # RGB average value, total accumulated RGB value divided by number of nearby pixel
            pixel.red = total_red / num
            pixel.green = total_green / num
            pixel.blue = total_blue / num

    return new_img


def main():
    """
    Function: To blur the imported image which the level of blurring can be adjusted
    Principle:Showing original image and activate the "blur" function and use for loop to adjust the layer(level)
    of blurring
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
