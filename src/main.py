from graphics import Window, Line, Point

def main():
    win = Window(800, 600)
    line1 = Line(Point(0, 100), Point(100, 1))
    win.draw_line(line1, 'black')
    win.wait_for_close()

main()