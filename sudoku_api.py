from input_parser import InputParser


class SudokuAPI:
    def __init__(self):
        pass

    @staticmethod
    def row(line_index, matrix_index, line_index_in_matrix, parser: InputParser):
        line = parser.get_line(line_index=line_index, matrix_index=line_index_in_matrix, except_index=matrix_index)
        print(line)

    @staticmethod
    def col(col_index, matrix_index, col_index_in_matrix, parser: InputParser):
        col = parser.get_col(col_index, matrix_index, col_index_in_matrix)
        # print(col)
    # @staticmethod
    # def col(col_index):
