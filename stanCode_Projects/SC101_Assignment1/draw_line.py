"""
File: draw_line
Name:Wei
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 30
c_1 = 0
x1 = str
y1 = str
window = GWindow()


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """

    onmouseclicked(point_and_line)


def point_and_line(mouse):
    """
    FUNCTION: The function can draw line by clicking twice of mouse.
    First click a circle will be created, second click a line will be created link to first clicking position and the
    second position. The circle create at first click will be removed every second click.
    PRINCIPLE: A parameter is set to differentiate if the clicking number is odd or even. By doing so, if statement is
    utilised to take drawing circle, line and removing action. Bunch of parameter should made global.

    """
    global x1
    global y1
    global c_1
    point1 = GOval(SIZE, SIZE)
    point1.color = 'black'

    if c_1 % 2 == 0:  # When clicking even, drawing circle
        window.add(point1, x=mouse.x - point1.width / 2, y=mouse.y - SIZE / 2)
        x1 = mouse.x
        y1 = mouse.y
        c_1 += 1
    else:   # When clicking odd, drawing line and remove previous circle
        remove_object = window.get_object_at(x1, y1)  # the circle should defined as another object to be remove
        window.remove(remove_object)
        line1 = GLine(x1, y1, mouse.x, mouse.y)
        line1.color = 'black'
        window.add(line1)
        c_1 += 1


if __name__ == "__main__":
    main()
