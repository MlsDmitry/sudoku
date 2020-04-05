class InputParser:
    def __init__(self, filename):
        self.file = open(filename)
        self.side_length = int(self.file.readline().strip())
        self.cell_length = int(self.file.readline().strip())
        self.sudoku = []

    def get_input(self):
        for line in self.file.readlines():
            line = line.strip()
            if line == '':
                break
            self.sudoku.append([int(i) for i in line if i != ' '])
        return self.sudoku

    def row(self, row):
        try:
            return set(self.sudoku[row])
        except Exception as e:
            print(e)

    def col(self, col):
        return {line[col] for line in self.sudoku}

    def get_square(self, row, col):
        col_section = col // self.cell_length
        row_section = row // self.cell_length
        # -----------------SLICES-------------------
        start_x = col_section * self.cell_length
        stop_x = col_section * self.cell_length + self.cell_length

        start_y = row_section * self.cell_length
        stop_y = row_section * self.cell_length + self.cell_length
        # -----------------END SLICES-------------------
        for y in range(start_y, stop_y):
            yield self.sudoku[y][start_x: stop_x]
