from input_parser import InputParser
from pprint import pprint


class SudokuAnalyzer:

    @staticmethod
    def analyze(field, parser: InputParser, row_section, col_section):
        available = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        scores = dict()
        for i, y in enumerate(field):
            row = parser.row(row_section + i)
            for j, x in enumerate(y):
                if x == 0:
                    col = parser.col(col_section + j)
                    scores[i, j] = (row | col)
                elif x in available:
                    available.remove(x)

        # ! ----------------------------------------

        for i, x in scores:
            scores[i, x] = available.difference(scores[i, x])

        return scores

    @staticmethod
    def recursive_fill_fields(scores, sudoku):
        pass

    @staticmethod
    def fill_cell(row, col, n, scores, sudoku: list):
        sudoku[row][col] = n
        return scores[row, col].remove(n)


parser_obj = InputParser('test1')

ret = parser_obj.get_input()
matrix = parser_obj.get_square(3, 0)  # return generator
# for i in matrix:
#     print(i)
scores = SudokuAnalyzer.analyze(matrix, parser_obj, 3, 0)
pprint(scores)
# SudokuAnalyzer.recursive_fill_fields(scores, ret)
