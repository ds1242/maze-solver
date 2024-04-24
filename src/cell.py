from graphics import Line, Point
class Cell:
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._visited = False
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = window
    
    def draw(self, x1, y1, x2, y2):  
        if self._win is None:
            return      
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "white")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "white")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "white")



    def draw_move(self, to_cell, undo=False):
        half_length = abs(self._x2 - self._x1) // 2
        self_center_x = half_length + self._x1 
        self_center_y = half_length + self._y1

        half_length2 = abs(to_cell._x2 - to_cell._x1) // 2
        to_cell_center_x = half_length2 + to_cell._x1 
        to_cell_center_y = half_length2 + to_cell._y1
     
        color = 'red' 
        if undo:
            color = 'gray'
            
        move_line = Line(Point(self_center_x, self_center_y), Point(to_cell_center_x, to_cell_center_y)) 
        self._win.draw_line(move_line, color)


   
