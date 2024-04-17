from graphics import Window, Line, Point

def main():
    win = Window(800, 600)
    point1 = Point(0, 100)
    point2 = Point(100, 1)
    point3 = Point(2, 20)
    point4 = Point(20, 2)
    line1 = Line(point1, point2)
    line2 = Line(point3, point4)
    win.draw_line(line1, 'black')
    win.draw_line(line2, 'black')
    win.wait_for_close()

main()