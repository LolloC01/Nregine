from random import randint
from provamatrice import get_diagonals

chess = [[0 for y in range(8)] for x in range(8)]

s: list = []


no_queen = {
    0 : [0, 1, 2, 3, 4, 5, 6, 7],
    1 : [0, 1, 2, 3, 4, 5, 6, 7],
    2 : [0, 1, 2, 3, 4, 5, 6, 7],
    3 : [0, 1, 2, 3, 4, 5, 6, 7],
    4 : [0, 1, 2, 3, 4, 5, 6, 7],
    5 : [0, 1, 2, 3, 4, 5, 6, 7],
    6 : [0, 1, 2, 3, 4, 5, 6, 7],
    7 : [0, 1, 2, 3, 4, 5, 6, 7]
}

def restart() -> dict:
    queen = {
        0 : [0, 1, 2, 3, 4, 5, 6, 7],
        1 : [0, 1, 2, 3, 4, 5, 6, 7],
        2 : [0, 1, 2, 3, 4, 5, 6, 7],
        3 : [0, 1, 2, 3, 4, 5, 6, 7],
        4 : [0, 1, 2, 3, 4, 5, 6, 7],
        5 : [0, 1, 2, 3, 4, 5, 6, 7],
        6 : [0, 1, 2, 3, 4, 5, 6, 7],
        7 : [0, 1, 2, 3, 4, 5, 6, 7]
    }
    return queen

def print_chess() -> None:
    for x in chess:
        print(x)

def check(pos: tuple) -> bool:
    for raw in range(8):
        if chess[raw][pos[1]] == 1:
            return False
    for raw in range(8):
        if chess[pos[0]][raw] == 1:
            return False
    diag1, diag2 = get_diagonals(chess, pos)
    if 1 in diag1:
        return False
    if 1 in diag2:
        return False
    return True

def chek_pos(x: int) -> list:
    """crea la lista con le posizioni in cui è possibile mettere una regina

    Args:
        x (int): indica la riga da controllare

    Returns:
        ris (list): lista di tuple contenente le posizioni possibili
    """
    ris = []
    for y in range(8):
        if check(x,y):
            ris.append((x,y))
    return ris

def prima_riga() -> None:
    y = randint(0,7)
    s.append((0,y))
    chess[0][y] = 1

def check_last_row() -> bool:
    pos = chek_pos()
    if len(pos) != 0:
        return True
    return False

def righe() -> None:
    pass

def n_queens(row: int, avanti: bool = True) -> bool:
    if avanti:
        if row == 0:
            prima_riga()
        elif row == 7:    ###Check ultima riga: se ci sono posizioni in cui mettere la regina ho finito altrimenti torno indietro
            pos = chek_pos(7)
            if len(pos) != 0:
                chess[7][pos[0]]
                s.append((7,pos(0)))
                return s
            else:
                pass ###ROLLBACK
        else:
            pos = chek_pos(row)
            if len(pos) != 0:
    else:
        pass