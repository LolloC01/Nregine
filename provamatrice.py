def get_diagonals(matrix: list[list[int]], pos: tuple) -> tuple[list[int]]:
    """
    ritorna la diagonale principale e l'antidiagonale della matrice data la posizione pos

    Args:
        matrix (list[list[int]]): matrice in cui cercare la posizione
        pos (tuple): posizione da cercare

    Returns:
        tuple[list[int]]: lista di tuple contenenti diagonale e anti-diagonale
    """
    row: int = pos[0]
    col: int = pos[1]

    diagonal: list[int] = []
    anti_diagonal: list[int] = []

    matrix_size: int = len(matrix)

    # Calcolo della diagonale
    if row < col:
        for r, c in zip(range(0, matrix_size), range(col - row, matrix_size)):
            diagonal.append(matrix[r][c])
    else:
        for r, c in zip(range(row - col, matrix_size), range(0, matrix_size)):
            diagonal.append(matrix[r][c])

    # Calcolo della anti-diagonale
    if row + col < 7:
        start_row = 0
        start_col = row + col
    else:
        start_row = row + col - 7
        start_col = 7

    while start_row < matrix_size and start_col >= 0:
        anti_diagonal.append(matrix[start_row][start_col])
        start_row += 1
        start_col -= 1

    return diagonal, anti_diagonal