"""
File: sierpinski.py
Name: Wei
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER =6                 # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	TODO:
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: the layer of Sierpinski triangle which appears recursively as 3 times and half edge-length inside
	the former layer triangle
	:param length: The edge length of the triangle
	:param upper_left_x: The x-coordinate of the top-left peak point of triangle
	:param upper_left_y: The y-coordinate of the top-left peak point of triangle
	:return: Sierpinski triangle as a fractal
	"""
	if order == 0:
		pass
	else:
		trian_1 = GLine(upper_left_x, upper_left_y, upper_left_x+length, upper_left_y)
		trian_2 = GLine(upper_left_x, upper_left_y, upper_left_x+length*0.5, upper_left_y+length*0.866)
		trian_3 = GLine(upper_left_x+length, upper_left_y, upper_left_x+length*0.5, upper_left_y+length*0.866)
		window.add(trian_1)
		window.add(trian_2)
		window.add(trian_3)

		# Upper left
		sierpinski_triangle(order-1, length/2, upper_left_x, upper_left_y)
		# Upper Right
		sierpinski_triangle(order-1, length/2, upper_left_x+length*0.5, upper_left_y)
		# bottom
		sierpinski_triangle(order-1, length/2, upper_left_x+length*0.25, upper_left_y+length*0.433)



if __name__ == '__main__':
	main()