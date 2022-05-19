"""
File: bouncing_ball
Name:Wei
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLabel
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 20
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
switcher = 1
count = 0


window = GWindow(800, 500, title='bouncing_ball.py')


def main():
    global switcher
    global count
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(ball_trigger)
    vy = 0

    ball_global = create_ball()
    window.add(ball_global, x=START_X, y=START_Y)


    while True:  # The program will
        pause(DELAY)
        while ball_global.x+ball_global.width <= window.width and switcher < 0:
            vy += GRAVITY
            # print(str(vy)) Just for checking the changing of velocity
            if count > 3:  # Ball will only fall for three time click
                break
            else:
                ball_global.move(VX, vy)
                pause(DELAY)
                if ball_global.y > window.height:
                    vy = -vy
                    vy *= REDUCE
        else:
            switcher = 0
            # print("count:" + str(count), "switcher"+str(switcher))   # Just for observing the nature of loop
            window.add(ball_global, x=START_X, y=START_Y)



def create_ball():
    """
    FUNCTION: To create ball
    PRINCIPLE: Using campy package GOval to create the ball
    """
    ball = GOval(SIZE, SIZE)
    ball.filled = True
    ball.fill_color = 'black'
    return ball


def ball_trigger(mouse):
    """
    FUNCTION: As a switcher to control if the ball start to falling and a count is set to control the time limitation
    PRINCIPLE: Link to a global parameter and manipulate its value using "get_object_at" conditional expression, by
    doing so when the value change and meet the condition set in While loop in main function, the ball is activated
    """
    global switcher
    global count

    trigger_object = window.get_object_at(mouse.x, mouse.y)
    if trigger_object is None:
        switcher = -3  # Any value smaller than zero
        count += 1
    return switcher
    return count







if __name__ == "__main__":
    main()