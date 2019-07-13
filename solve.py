a = [
    [0, 4, 5, 0, 9, 0, 0, 7, 0],
    [1, 0, 7, 3, 0, 6, 5, 0, 8],
    [0, 9, 0, 2, 7, 0, 0, 6, 1],
    [0, 1, 0, 0, 2, 0, 3, 8, 0],
    [2, 0, 8, 4, 1, 9, 6, 0, 7],
    [0, 6, 9, 0, 5, 0, 0, 4, 0],
    [4, 5, 0, 0, 8, 2, 0, 3, 0],
    [9, 0, 6, 5, 0, 1, 7, 0, 4],
    [0, 7, 0, 0, 6, 0, 8, 1, 0]
]
""" a = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
] """
b = a


def input_value(x, y, value):
    for i in range(1, 10):
        if value == b[x][i-1] or value == b[i-1][y] or value == b[(x//3)*3+((i-1)//3)][(y//3)*3+((i-1) % 3)]:
            return False
    return True


def move_next(x, y):
    if x == 8 and y == 8:
        return True
    else:
        if x == 8:
            if solve(0, y + 1):
                return True
        else:
            if solve(x + 1, y):
                return True


def solve(x=0, y=0):
    if b[x][y] == 0:
        for i in range(1, 10):
            if input_value(x, y, i):
                b[x][y] = i
                if move_next(x, y):
                    return True
        b[x][y] = 0
        return False
    else:
        if move_next(x, y):
            return True


def print_board(board):
    for line in board:
        for value in line:
            if value != 0:
                print(value, end='')
            else:
                print(' ', end='')
        print("")


print_board(a)
if solve():
    print("")
    print("")
    print_board(b)
else:
    print("Cant solve!!!")
