from graphics import Window, Line, Point, Cell

def main():
    win = Window(800, 600)
    cell_1 = Cell(Point(100,100), Point(200,200), win)
    cell_1.draw()
    # win.draw_line(line1, 'black')
    win.wait_for_close()

main()