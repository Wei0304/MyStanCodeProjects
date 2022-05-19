"""
File: stanCodoshop.py
Name: Wei
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """

    red_pixel = pixel.red
    green_pixel = pixel.green
    blue_pixel = pixel.blue

    color_distance = ((red-red_pixel)**2 + (green-green_pixel)**2 + (blue-blue_pixel)**2)**0.5
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """

    total_red_pixel = 0
    total_green_pixel = 0
    total_blue_pixel = 0


    for i in range(len(pixels)):  # 一次丟很多個Pixels
        pixel = pixels[i]
        red_pixel = pixel.red
        green_pixel = pixel.green
        blue_pixel = pixel.blue

        total_red_pixel += red_pixel
        total_green_pixel += green_pixel
        total_blue_pixel += blue_pixel


    avg_red = total_red_pixel // len(pixels)
    avg_green = total_green_pixel // len(pixels)
    avg_blue = total_blue_pixel // len(pixels)

    avg_list = [avg_red, avg_green, avg_blue]

    return avg_list




def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    dis = 0
    count = 0

    for i in range(len(pixels)):
        dis_color = get_pixel_dist(pixels[i], get_average(pixels)[0], get_average(pixels)[1], get_average(pixels)[2])
        if dis == 0:  # first round
            dis = dis_color
        else:
            if dis_color < dis:
                dis = dis_color
                count += 1  # to get the right pixel out from the list

    return pixels[count]


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """

    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)


        # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect
    for x in range(width):
        for y in range(height):
            result_pix = result.get_pixel(x, y)  # each pixel on the result canvas
            list_ = []
            for image in images:
                pix = image.get_pixel(x, y)
                list_.append(pix)
            best_pix = get_best_pixel(list_)  # return Pixel

            result_pix.red = best_pix.red
            result_pix.blue = best_pix.blue
            result_pix.green = best_pix.green


    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
