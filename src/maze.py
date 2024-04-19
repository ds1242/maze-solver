from cell import Cell

class Maze:
    def __init__(
            self, 
            x1, 
            y1, 
            num_rows,
            num_cols, 
            cell_size_x, 
            cell_size_y, 
            win
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()

        def _create_cells(self):
            self._cells = []

            for i in range(self.num_cols):
                temp = []
                for j in range(self.num_rows):
                    cell = Cell(self.win)
                    temp.append(cell)
                self._cells.append(temp)

            for i in range(len(self._cells)):
                column = self._cells[i]

                for j in range(len(column)):
                    self._draw_cell(i,j)


        def _draw_cell(self, i, j):
            
            self._animate()
            
        def _animate(self):
            pass

            


