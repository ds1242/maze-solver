from graphics import Window, Line, Point

def main():
    win = Window(800, 600)
    win.wait_for_close()
    point1 = Point(0, 10)
    point2 = Point(10, 1)
    point3 = Point(2, 20)
    point4 = Point(20, 2)
    line1 = Line(point1, point2)
    line2 = Line(point3, point4)
    win.draw_line(line1, 'black')

main()