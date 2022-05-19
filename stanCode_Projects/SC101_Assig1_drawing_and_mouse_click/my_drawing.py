"""
File: my_drawing
Name:Wei
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GLabel, GPolygon
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: Neon Sunset
    創作理念: 寫作業時很喜歡聽vaporwave類型的音樂，只要是這種音樂都會伴隨霓虹帶點Cyberpunk風格的日落影片，覺得用python畫出來特別有味道
    """
    window = GWindow(width=500, height=500, title="Neon sunset")
    background = GRect(800, 500, x=0, y=0)
    window.add(background)
    sun = GOval(120, 120, x=window.width/2-60, y=120)
    window.add(sun)
    block = GRect(100, 100, x=200, y=220)
    window.add(block)
    horizon0 = GLine(0, 220, 500, 220)
    window.add(horizon0)
    horizon1 = GLine(0, 225, 500, 225)  # 5
    window.add(horizon1)
    horizon2 = GLine(0, 235, 500, 235)  # 10
    window.add(horizon2)
    horizon3 = GLine(0, 250, 500, 250)  # 15
    window.add(horizon3)
    horizon4 = GLine(0, 275, 500, 275)  # 25
    window.add(horizon4)
    horizon5 = GLine(0, 310, 500, 310)  # 35
    window.add(horizon5)
    horizon6 = GLine(0, 355, 500, 355)  # 45
    window.add(horizon6)
    horizon7 = GLine(0, 415, 500, 415)  # 60
    window.add(horizon7)
    horizon8 = GLine(0, 485, 500, 485)  # 70
    window.add(horizon8)

    vertical0 = GLine(210, 220, -150, 500)
    window.add(vertical0)
    vertical1 = GLine(220, 220, 0, 500)
    window.add(vertical1)
    vertical2 = GLine(230, 220, 100, 500)
    window.add(vertical2)
    vertical3 = GLine(240, 220, 190, 500)
    window.add(vertical3)
    vertical4 = GLine(260, 220, 310, 500)
    window.add(vertical4)
    vertical5 = GLine(270, 220, 400, 500)
    window.add(vertical5)
    vertical6 = GLine(280, 220, 500, 500)
    window.add(vertical6)
    vertical7 = GLine(290, 220, 650, 500)
    window.add(vertical7)

    # Building 0
    build0_0 = GPolygon()
    build0_0.add_vertex((100, 220))  # 左上
    build0_0.add_vertex((100, 300))  # 左下
    build0_0.add_vertex((120, 290))  # 右下
    build0_0.add_vertex((120, 210))  # 右上
    build0_1 = GPolygon()
    build0_1.add_vertex((-10, 215))  # 左上
    build0_1.add_vertex((-10, 295))  # 左下
    build0_1.add_vertex((100, 300))  # 右下
    build0_1.add_vertex((100, 220))  # 右上
    build0_2 = GPolygon()
    build0_2.add_vertex((-10, 215))  # 左下
    build0_2.add_vertex((100, 220))  # 右下
    build0_2.add_vertex((120, 210))  # 右上
    build0_2.add_vertex((10, 205))  # 左上

    # Building 1
    build1_0 = GPolygon()
    build1_0.add_vertex((135, 180))  # 左上
    build1_0.add_vertex((135, 250))  # 左下
    build1_0.add_vertex((145, 240))  # 右下
    build1_0.add_vertex((145, 170))  # 右上
    build1_1 = GPolygon()
    build1_1.add_vertex((80, 177))  # 左上
    build1_1.add_vertex((80, 247))  # 左下
    build1_1.add_vertex((135, 250))  # 右下
    build1_1.add_vertex((135, 180))  # 右上
    build1_2 = GPolygon()
    build1_2.add_vertex((80, 177))  # 左下
    build1_2.add_vertex((135, 180))  # 右下
    build1_2.add_vertex((145, 170))  # 右上
    build1_2.add_vertex((90, 167))  # 左上

    # Building 2
    build2_0 = GPolygon()
    build2_0.add_vertex((450, 300))  # 左上
    build2_0.add_vertex((450, 400))  # 左下
    build2_0.add_vertex((600, 590))  # 右下
    build2_0.add_vertex((600, 400))  # 右上

    build2_2 = GPolygon()
    build2_2.add_vertex((600, 400))  # 左下
    build2_2.add_vertex((600, 350))  # 右下
    build2_2.add_vertex((600, 290))  # 右上
    build2_2.add_vertex((450, 300))  # 左上

    window.add(build1_0)
    window.add(build1_1)
    window.add(build1_2)
    window.add(build0_0)
    window.add(build0_1)
    window.add(build0_2)
    window.add(build2_0)
    window.add(build2_2)

    # Mountain
    Mount1 = GPolygon()
    Mount1.add_vertex((380, 180))  # 上
    Mount1.add_vertex((360, 220))  # 左下
    Mount1.add_vertex((385, 210))  # 右下
    Mount2 = GPolygon()
    Mount2.add_vertex((360, 220))  # 左上
    Mount2.add_vertex((385, 210))  # 右上
    Mount2.add_vertex((380, 250))  # 下
    Mount3 = GPolygon()
    Mount3.add_vertex((360, 220))  # 上
    Mount3.add_vertex((360, 240))  # 左下
    Mount3.add_vertex((380, 250))  # 右下
    Mount4 = GPolygon()
    Mount4.add_vertex((360, 220))  # 上
    Mount4.add_vertex((320, 250))  # 左下
    Mount4.add_vertex((360, 240))  # 右下
    Mount5 = GPolygon()
    Mount5.add_vertex((380, 180))  # 上
    Mount5.add_vertex((385, 210))  # 左下
    Mount5.add_vertex((390, 200))  # 右下
    Mount6 = GPolygon()
    Mount6.add_vertex((385, 210))  # 左上
    Mount6.add_vertex((390, 200))  # 右上
    Mount6.add_vertex((430, 215))  # 下
    Mount7 = GPolygon()
    Mount7.add_vertex((385, 210))  # 左上
    Mount7.add_vertex((430, 215))  # 右上
    Mount7.add_vertex((380, 250))  # 下
    Mount8 = GPolygon()
    Mount8.add_vertex((380, 250))  # 左上
    Mount8.add_vertex((430, 215))  # 右上
    Mount8.add_vertex((450, 260))  # 下


    window.add(Mount1)
    window.add(Mount2)
    window.add(Mount3)
    window.add(Mount4)
    window.add(Mount5)
    window.add(Mount6)
    window.add(Mount7)
    window.add(Mount8)

    # shadow
    shadow1 = GPolygon()
    shadow1.add_vertex((150, 215))  # 左下
    shadow1.add_vertex((350, 215))  # 右下
    shadow1.add_vertex((350, 212))  # 右上
    shadow1.add_vertex((150, 212))  # 左上
    shadow2 = GPolygon()
    shadow2.add_vertex((150, 207))  # 左下
    shadow2.add_vertex((350, 207))  # 右下
    shadow2.add_vertex((350, 205))  # 右上
    shadow2.add_vertex((150, 205))  # 左上
    shadow3 = GPolygon()
    shadow3.add_vertex((150, 199))  # 左下
    shadow3.add_vertex((350, 199))  # 右下
    shadow3.add_vertex((350, 197))  # 右上
    shadow3.add_vertex((150, 197))  # 左上
    shadow4 = GPolygon()
    shadow4.add_vertex((150, 191))  # 左下
    shadow4.add_vertex((350, 191))  # 右下
    shadow4.add_vertex((350, 189))  # 右上
    shadow4.add_vertex((150, 189))  # 左上
    shadow5 = GPolygon()
    shadow5.add_vertex((150, 183))  # 左下
    shadow5.add_vertex((350, 183))  # 右下
    shadow5.add_vertex((350, 181))  # 右上
    shadow5.add_vertex((150, 181))  # 左上

    window.add(shadow1)
    window.add(shadow2)
    window.add(shadow3)
    window.add(shadow4)
    window.add(shadow5)

    # background, sun and grid line
    background.filled = True
    background.fill_color = 'black'
    sun.filled = True
    sun.fill_color = 'gold'
    sun.color = 'gold'
    block.filled = True
    block.fill_color = 'black'
    horizon0.color = 'magenta'
    horizon1.color = 'magenta'
    horizon2.color = 'magenta'
    horizon3.color = 'magenta'
    horizon4.color = 'magenta'
    horizon5.color = 'magenta'
    horizon6.color = 'magenta'
    horizon7.color = 'magenta'
    vertical0.color = 'magenta'
    vertical1.color = 'magenta'
    vertical2.color = 'magenta'
    vertical3.color = 'magenta'
    vertical4.color = 'magenta'
    vertical5.color = 'magenta'
    vertical6.color = 'magenta'
    vertical7.color = 'magenta'

    # Shadow
    shadow1.filled = True
    shadow1.fill_color = 'black'
    shadow1.color = 'black'
    shadow2.filled = True
    shadow2.fill_color = 'black'
    shadow2.color = 'black'
    shadow3.filled = True
    shadow3.fill_color = 'black'
    shadow3.color = 'black'
    shadow4.filled = True
    shadow4.fill_color = 'black'
    shadow4.color = 'black'
    shadow5.filled = True
    shadow5.fill_color = 'black'
    shadow5.color = 'black'

    # Building 1
    build1_0.filled = True
    build1_0.fill_color = 'black'
    build1_0.color = 'blue'
    build1_1.filled = True
    build1_1.fill_color = 'black'
    build1_1.color = 'blue'
    build1_2.filled = True
    build1_2.fill_color = 'black'
    build1_2.color = 'blue'

    # Building 0
    build0_0.filled = True
    build0_0.fill_color = 'black'
    build0_0.color = 'blue'
    build0_1.filled = True
    build0_1.fill_color = 'black'
    build0_1.color = 'blue'
    build0_2.filled = True
    build0_2.fill_color = 'black'
    build0_2.color = 'blue'

    # Building 2
    build2_0.filled = True
    build2_0.fill_color = 'black'
    build2_0.color = 'blue'
    build2_2.filled = True
    build2_2.fill_color = 'black'
    build2_2.color = 'blue'

    # Mountain
    Mount1.filled = True
    Mount1.fill_color = 'black'
    Mount1.color = 'lime green'
    Mount2.filled = True
    Mount2.fill_color = 'black'
    Mount2.color = 'lime green'
    Mount3.filled = True
    Mount3.fill_color = 'black'
    Mount3.color = 'lime green'
    Mount4.filled = True
    Mount4.fill_color = 'black'
    Mount4.color = 'lime green'
    Mount5.filled = True
    Mount5.fill_color = 'black'
    Mount5.color = 'lime green'
    Mount6.filled = True
    Mount6.fill_color = 'black'
    Mount6.color = 'lime green'
    Mount7.filled = True
    Mount7.fill_color = 'black'
    Mount7.color = 'lime green'
    Mount8.filled = True
    Mount8.fill_color = 'black'
    Mount8.color = 'lime green'

    text = GLabel("welcome to neon world", 200, 100)
    text.font = 'courier-20'
    text.color = 'Magenta'
    window.add(text, 80, 70)


if __name__ == '__main__':
    main()
