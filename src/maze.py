from cell import Cell
import random
import time

class Maze:
    def __init__(
            self, 
            x1, 
            y1, 
            num_rows,
            num_cols, 
            cell_size_x, 
            cell_size_y, 
            win=None,
            seed=None
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)
            
        
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        
    def _create_cells(self):
        for i in range(self._num_cols):
            temp = []
            for j in range(self._num_rows):
                cell = Cell(self._win)
                temp.append(cell)
            self._cells.append(temp)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i,j)


    def _draw_cell(self, i, j):
        if self._win is None:
            return 
        
        top_left_x = self._x1 + i * self._cell_size_x
        top_left_y = self._y1 + j * self._cell_size_y

        bottom_right_x = top_left_x + self._cell_size_x
        bottom_right_y = top_left_y + self._cell_size_y

        self._cells[i][j].draw(top_left_x, top_left_y, bottom_right_x, bottom_right_y)
        self._animate()
        
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)


    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)
    
    def _break_walls_r(self, i, j):
        self._cells[i][j]._visited = True
        while True:
            possible_directions = []
            #left
            if i > 0 and not self._cells[i - 1][j]._visited:
                possible_directions.append((i - 1, j))
            # right
            if i < self._num_cols - 1 and not self._cells[i + 1][j]._visited:
                possible_directions.append((i + 1, j))
            # up
            if j > 0 and not self._cells[i][j - 1]._visited:
                possible_directions.append((i, j - 1))
            # down
            if j < self._num_rows - 1 and not self._cells[i][j + 1]._visited:
                possible_directions.append((i, j + 1))

            if len(possible_directions) == 0:
                self._draw_cell(i,j)
                return
               
            direction_index = random.randrange(len(possible_directions))
            next_index = possible_directions[direction_index]

            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
            
            # recursively visit the next cell
            self._break_walls_r(next_index[0], next_index[1])

    def _reset_cells_visited(self):
        pass
