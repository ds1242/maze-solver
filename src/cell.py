from graphics import Line, Point
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

    def draw_move(self, to_cell, undo=False):
        if undo == False:
            color = 'red'
        else:
            color = 'gray'

        self_center.x = (self._x1 + self._x2) // 2
        self_center.y = (self._y1 + self._y2) // 2
        to_cell_center.x = (to_cell._x1 + to_cell._x2) // 2
        to_cell_center.y = (to_cell._y1 + to_cell._y2) // 2
     
        move_line = Line(Point(self_center.x, self_center.y), Point(to_cell_center.x, to_cell_center.y) 
        self._win.draw_line(move_line, color)



