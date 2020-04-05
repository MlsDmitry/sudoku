import sys

sys.path.append('/Users/mlsdmitry/Documents/sudoky/scripts/tests/')

# from scripts.sudoku_api import SudokuAPI
# from scripts.input_parser import InputParser

# parser = InputParser('/Users/mlsdmitry/Documents/sudoky/scripts/test1')
# parser.get_input(3)
# SudokuAPI.row(2, 1, 1, parser)
# SudokuAPI.col(2, 2, 5, parser)

# print(open('/Users/mlsdmitry/Documents/sudoky/scripts/test1').readlines())

a = {(0, 0): {2}, (2, 0): {8, 5}}
print(a.values())
print(a.keys())
print(a.items())
print(sorted(a.items(), key=lambda k: len(k[1])))



# [0, 3, 0]
# [1, 6, 9]
# [0, 4, 0]
#       (0, 0): {2}
#       (0, 2): {7}
#       (2, 0): {8, 5}
#       (2, 2): {8, 5}

# [6, 1, 2]
# [4, 0, 3]
# [0, 8, 0]

#       (1, 1): {7}
#       (2, 0): {9, 5}
#       (2, 2): {5}

# [7, 0, 6]
# [3, 9, 0]
# [0, 5, 4]


def pp(value):
    print(f'[pp] - {value}')
