from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.__root, bg='white', width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=1)
        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print('window closed!')

    def close(self):
        self.__running = False
    
    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point_1, point_2):
        self.x1 = point_1.x
        self.y1 = point_1.y
        self.x2 = point_2.x
        self.y2 = point_2.y

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.x1, self.y1, self.x2, self.y2, fill=fill_color, width=2
        )
        canvas.pack(fill=BOTH, expand=1)


class Cell:
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = window
    
    def draw(self, x1, y1, x2, y2):        
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_left_wall:
            wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(wall, "black")
        if self.has_right_wall:
            wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(wall, "black")
        if self.has_top_wall:
            wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(wall, "black")
        if self.has_bottom_wall:
            wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(wall, "black")