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
            splited = line.split()
            self.sudoku.append(list(list(map(int, list(i))) for i in splited))
        # pprint(self.sudoku)
        return self.sudoku

    def row(self, row_index):
        try:
            return {j for i in self.sudoku[row_index] for j in i}
        except Exception as e:
            print(e)

    def col(self, col_index, second_party_col_index):
        return {line[col_index][second_party_col_index] for line in self.sudoku}

    def get_square(self, row, col):
        col_section = col // self.cell_length
        row_section = row // self.cell_length
        for y in range(row_section * self.cell_length, row_section * self.cell_length + self.cell_length):
            yield self.sudoku[y][col_section]

    def as_string(self):
        pprint(self.sudoku)
    # for i in range(self.side_length * self.side_length):
    #     print(self.sudoku[i])


parser = InputParser('../test1')
ret = parser.get_input()
pprint(ret)
print(parser.row(0))
print(parser.col(1, 1))
for i in parser.get_square(2, 1):
    print(i)