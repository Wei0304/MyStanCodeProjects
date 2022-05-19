"""
File: babygraphics.py
Name: Wei
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    space = (width - 2*GRAPH_MARGIN_SIZE)/len(YEARS)
    x_coordinate = GRAPH_MARGIN_SIZE + year_index*space
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    for i in range(len(YEARS)):
        year = YEARS[i]
        x_coord = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x_coord, 0, x_coord, CANVAS_HEIGHT)
        canvas.create_text(x_coord, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=year, anchor=tkinter.NW)



def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    for i in range(len(lookup_names)):
        for j in range(len(YEARS)-1):
            if i < len(COLORS):  # To make the color index return to zero when exceeds
                color = COLORS[i]
            else:
                a = i / len(COLORS)
                color = COLORS[i-len(COLORS)*int(a)]

            name = lookup_names[i]
            x_1 = get_x_coordinate(CANVAS_WIDTH, j)
            x_2 = get_x_coordinate(CANVAS_WIDTH, j+1)

            year_1 = YEARS[j]
            if name in name_data and str(year_1) in name_data[name]:
                y_1 = (int((name_data[name][str(year_1)])) / MAX_RANK * (CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE))+GRAPH_MARGIN_SIZE
                canvas.create_text(x_1, y_1, text=name + " " + str(name_data[name][str(year_1)]), anchor=tkinter.SW, fill=color)
            else:
                y_1 = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                canvas.create_text(x_1, y_1, text=name + " *", anchor=tkinter.SW, fill=color)

            year_2 = YEARS[j + 1]
            if name in name_data and str(year_2) in name_data[name]:
                y_2 = (int((name_data[name][str(year_2)])) / MAX_RANK * (CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE))+GRAPH_MARGIN_SIZE
                if j == 10:
                    canvas.create_text(x_2, y_2, text=name + " " + str(name_data[name][str(year_2)]), anchor=tkinter.SW, fill=color)
            else:
                y_2 = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                if j == 10:
                    canvas.create_text(x_2, y_2, text=name + " *", anchor=tkinter.SW, fill=color)

            canvas.create_line(x_1, y_1, x_2, y_2, width=LINE_WIDTH, fill=color)




# main() code is provided, feel free to read through it but DO NOT MODIFY


def main():


    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
