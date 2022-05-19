"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This is a game called Breakout which will remind you the simple happiness we used to have when we were kids.
The goal is to control the paddle to have the ball rebound and hit the colorful bricks, then the bricks will be broken
and disappeared.When all the bricks are removed, you win.
On the contrary, if you run out the number of lives which is 3 before removing all the bricks, you loose the game! So
be careful, don't let the ball fall on the bottom!

Wei 2022.3.24
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics


FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts


# Add the animation loop here!
def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES

    while True:
        pause(FRAME_RATE)
        if graphics.ball.y + graphics.ball.height >= graphics.window.height:
            lives -= 1
            print(graphics.count_brick())  # for checking how many bricks are removed
            if lives > 0:
                graphics.fall_off()
            else:
                graphics.game_over()
                break  # break all
        elif graphics.count_brick() == 100:  # When all the bricks are removed
            graphics.game_win()
            break
        graphics.change_direction()
        global_dx = graphics.getter_dx()
        global_dy = graphics.getter_dy()
        graphics.ball.move(global_dx, global_dy)
        graphics.check_collision()

    # print(str(count_num))



if __name__ == '__main__':
    main()
