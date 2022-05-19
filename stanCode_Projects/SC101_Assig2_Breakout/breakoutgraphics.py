"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

This package is for Breakout game
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball



class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):


        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(PADDLE_WIDTH, PADDLE_HEIGHT)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle, x=(self.window.width-self.paddle.width)/2, y=(self.window.height-PADDLE_OFFSET))

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2, y=(self.window.height-self.ball.height)/2)
        self.ball.filled = True

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Default bricks counter
        self._count = 0


        # Initialize our mouse listeners
        onmouseclicked(self.ball_start)
        onmousemoved(self.paddle_track)


        # Draw bricks
        for i in range(BRICK_COLS):
            for j in range(BRICK_ROWS):
                self.bricks = GRect(width=brick_width, height=brick_height)
                self.window.add(self.bricks, x=i*(self.bricks.width+BRICK_SPACING),
                                y=j*(self.bricks.height+BRICK_SPACING)+BRICK_OFFSET)
                if j == 0 or j == 1:
                    self.bricks.color = 'darkred'
                    self.bricks.filled = True
                    self.bricks.fill_color = 'darkred'

                if j == 2 or j == 3:
                    self.bricks.color = 'indianred'
                    self.bricks.filled = True
                    self.bricks.fill_color = 'indianred'

                if j == 4 or j == 5:
                    self.bricks.color = 'salmon'
                    self.bricks.filled = True
                    self.bricks.fill_color = 'salmon'

                if j == 6 or j == 7:
                    self.bricks.color = 'goldenrod'
                    self.bricks.filled = True
                    self.bricks.fill_color = 'goldenrod'

                if j == 8 or j == 9:
                    self.bricks.color = 'khaki'
                    self.bricks.filled = True
                    self.bricks.fill_color = 'khaki'

    # The paddle will follow movement of mouse at x axis, the position at y remain
    def paddle_track(self, mouse):
        x_1 = mouse.x-self.paddle.width/2
        if mouse.x >= self.window.width-self.paddle.width/2:  # Prevent left edge of paddle over the left boundary
            x_1 = mouse.x-(self.window.width-mouse.xself)
        if mouse.x <= self.paddle.width/2:  # Prevent right edge of paddle over the right boundary
            x_1 = 0

        self.window.add(self.paddle, x=x_1, y=(self.window.height - PADDLE_OFFSET))

    # Trigger the ball to move by clicking mouse
    def ball_start(self, mouse):
        if self.__dx == 0 or self.__dy == 0:
            self.__dy = INITIAL_Y_SPEED
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = - self.__dx

    # To rebound when ball hit the top, left and right boundary
    def change_direction(self):
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
            self.__dx = - self.__dx
        elif self.ball.y <= 0:
            self.__dy = - self.__dy

    # To define situation when ball fall off the bottom window, ball will appear at initial position
    def fall_off(self):
        if self.ball.y + self.ball.height >= self.window.height:
            self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2,
                            y=(self.window.height - self.ball.height) / 2)
            # to reset the initial ball velocity to trigger the onmouseclick function
            self.__dx = 0
            self.__dy = 0

    # getter (@property note: 若使用要去掉括弧)
    def getter_dx(self):
        return self.__dx

    # getter
    def getter_dy(self):
        return self.__dy

    # The condition when ball hit paddle or bricks.
    def check_collision(self):
        obj_1 = self.window.get_object_at(self.ball.x, self.ball.y)
        obj_2 = self.window.get_object_at(self.ball.x+2*BALL_RADIUS, self.ball.y)
        obj_3 = self.window.get_object_at(self.ball.x, self.ball.y+2*BALL_RADIUS)
        obj_4 = self.window.get_object_at(self.ball.x+2*BALL_RADIUS, self.ball.y+2*BALL_RADIUS)

        if obj_1 is not None:
            if obj_1 is self.paddle:
                # self.__dx = - self.__dx
                self.ball.move(0, -self.paddle.height)  # To avoid the ball get stock in the paddle
                self.__dy = - self.__dy

                # When hit the bricks
            else:
                self.window.remove(obj_1)
                self._count += 1  # To count the number of bricks hit
                self.__dx = - self.__dx
                self.__dy = - self.__dy

        elif obj_2 is not None:
            if obj_2 is self.paddle:
                # self.__dx = - self.__dx
                self.ball.move(0, -self.paddle.height)  # To avoid the ball get stock in the paddle
                self.__dy = - self.__dy

                # When hit the bricks
            else:
                self.window.remove(obj_2)
                self._count += 1
                self.__dx = - self.__dx
                self.__dy = - self.__dy

        elif obj_3 is not None:
            if obj_3 is self.paddle:
                # self.__dx = - self.__dx
                self.ball.move(0, -self.paddle.height)  # To avoid the ball get stock in the paddle
                self.__dy = - self.__dy

                # When hit the bricks
            else:
                self.window.remove(obj_3)
                self._count += 1
                self.__dx = - self.__dx
                self.__dy = - self.__dy

        elif obj_4 is not None:
            if obj_4 is self.paddle:
                # self.__dx = - self.__dx
                self.ball.move(0, -self.paddle.height)  # To avoid the ball get stock in the paddle
                self.__dy = - self.__dy

                # When hit the bricks
            else:
                self.window.remove(obj_4)
                self._count += 1
                self.__dx = - self.__dx
                self.__dy = - self.__dy

    # When number of live is run out, the whole game come to end
    def game_over(self):
        self.GG = GLabel('Game over')
        self.GG.font = 'calibri-40'
        self.window.add(self.GG, x=(self.window.width - self.ball.width) / 4,
                        y=(self.window.height - self.ball.height) / 2)

    # When all the bricks is removed, player win the game
    def game_win(self):
        self.win = GLabel('Congratulation. You win!')
        self.win.font = 'calibri-40'
        self.window.add(self.win, x=(self.window.width - self.ball.width) / 3,
                        y=(self.window.height - self.ball.height) / 2)

    # getter, to pass the number of bricks been hit
    def count_brick(self):
        return self._count


