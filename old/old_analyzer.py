from input_parser import InputParser


class SudokuAnalyzer:

    @staticmethod
    def analyze(field, parser: InputParser):
        available = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        scores = dict()
        for i, y in enumerate(field):
            row = parser.row(i)
            for x in y:
                if x == 0:
                    col = parser.col(x, y.index(x))
                    scores[i, x] = (row | col)
                elif x in available:
                    available.remove(x)

        # ! ----------------------------------------

        for i, x in scores:
            scores[i, x] = available.difference(scores[i, x])

        return scores

    @staticmethod
    def recursive_fill_fields(scores):
        pass

    @staticmethod
    def fill_cell(cell_row, cell_col, field_row, field_col, n, sudoku: list):
        sudoku[cell_row][cell_col][field_row][field_col] = n


parser_obj = InputParser('../test1')
parser_obj.cell_length = 3
parser_obj.side_length = 3
# analyzer = SudokuAnalyzer()
ret = parser_obj.get_input()
# print(*ret, sep='\n')
matrix = parser_obj.get_square(0, 0)

ret2 = SudokuAnalyzer.analyze(matrix, parser_obj)
# SudokuAnalyzer.fill_cell(0, 0, 0, 0, 4, ret)
# print(sud)
print(ret2)
