import numpy as np

#chess = [[0 for y in range(8)] for x in range(8)]

chess = []
for x in range(8):
    c = []
    for y in range(8):
        c.append(y)
    chess.append(c)

s: list = []

def check(pos: tuple) -> bool:
    """for raw in range(8):
        if chess[raw][pos[1]] == 1:
            return False
    for raw in range(8):
        if chess[pos[0]][raw] == 1:
            return False"""
    diag1 = np.diagonal(chess,pos[0])
    print(diag1)
    diag2 = np.fliplr(chess)
    diag_2 = np.diagonal(diag2,-pos[1])
    print(diag_2)
    return True
        

def print_m(chess: list) -> None:
    for x in chess:
        print(x)

chess[2][4] = 1
print_m(chess)
print(chess[2][4])
print(check((2,4)))