from pprint import pprint

N = 9
check_diagonal = False
mtx = [
    [0, 6, 0, 0, 0, 2, 0, 0, 7],
    [1, 0, 0, 0, 0, 0, 9, 0, 0],
    [0, 9, 0, 7, 0, 0, 1, 6, 3],
    [0, 0, 7, 0, 8, 0, 0, 0, 0],
    [4, 2, 0, 0, 0, 0, 0, 5, 8],
    [0, 0, 0, 0, 2, 0, 7, 0, 0],
    [7, 1, 5, 0, 0, 8, 0, 3, 0],
    [0, 0, 9, 0, 0, 0, 0, 0, 1],
    [3, 0, 0, 5, 0, 0, 0, 8, 0],
]

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
]

hard_one = [
    [0, 2, 0, 7, 0, 0, 0, 1, 0],
    [0, 5, 0, 0, 0, 3, 2, 0, 0],
    [0, 0, 9, 0, 5, 0, 0, 0, 8],
    [2, 1, 0, 0, 9, 0, 5, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 6, 0, 1, 0, 0, 4, 7],
    [5, 0, 0, 0, 4, 0, 3, 0, 0],
    [0, 0, 2, 1, 0, 0, 0, 6, 0],
    [0, 4, 0, 0, 0, 8, 0, 0, 0],
]
with_diagonal = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 7, 9, 6, 0, 0],
    [2, 0, 0, 0, 0, 0, 0, 3, 0],
    [3, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 4, 0, 0, 0, 0, 0, 2, 0],
    [0, 5, 0, 0, 0, 0, 0, 0, 7],
    [0, 6, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 7, 8, 9, 0, 0, 0, 5],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]


def add_and_check(mat, r, c, val):
    """Adds the val to mat[r]

    Args:
        mat (2d list): Matrix to solve
        r (int): row
        c (int): col
        val (int): value to be added|tested

    Returns:
        True: value is suitable for this position
        False: value is not suitable for this position
    """
    try:
        mat[r][c] = 0
        # check box
        row, col = r // 3 * 3, c // 3 * 3
        for row in mat[row : row + 3]:
            if val in row[col : col + 3]:
                return False
        # check row
        if val in mat[r]:
            return False
        # check col
        if val in [x[c] for x in mat]:
            return False
        # check diagonal
        if check_diagonal:
            if r == c:
                if val in [mat[i][i] for i in range(N)]:
                    return False
            M = N - 1
            if r + c == M:
                if val in [mat[i][M - i] for i in range(N)]:
                    return False
        return True
    except:
        print(r, c)
        raise

    finally:
        mat[r][c] = val


def is_done(mat):
    """Check if mat is a valid Sudoku solution

    """

    # check all rows
    for i in range(N):
        if set(x for x in mat[i] if x != 0).__len__() != N:
            return False

    # check all collumns
    for row in mat:
        if set(x for x in row if x != 0).__len__() != N:
            return False

    # check diagonal
    if check_diagonal:
        if set([mat[i][i] for i in range(N) if mat[i][i] != 0]).__len__() != N:
            return False
        M = N - 1
        if set([mat[i][M - i] for i in range(N) if mat[i][M - i] != 0]).__len__() != N:
            return False

    # check miniboxes
    for i in range(N):
        row, col = i // 3 * 3, i % 3 * 3
        ls = []
        for row in mat[row : row + 3]:
            ls.extend(row[col : col + 3])
        ls_set = set(x for x in ls if x)
        if ls_set.__len__() != N:
            return False

    return True
    """
    for i in range(N):
        for j in range(N):
            try:
                if not add_and_check(mat, i, j, mat[i][j]):
                    return False
            except:
                print(i, j)
                raise
    return True
    """


def make_sk(mat, cell=0):
    """Solves the Sudoku puzzle

    """
    # print(cell)
    if cell >= N * N: # we have solved all the cells
        return True
    r, c = cell // N, cell % N
    if mat[r][c] != 0: # fixed value
        return make_sk(mat, cell + 1)

    for v in range(1, 10):
        """ function add_and_check assigns v to mat[r][c]"""
        if add_and_check(mat, r, c, v):
            # we found a valid value for current cell
            # call for the next cell
            if make_sk(mat, cell + 1):
                # we have solved all the cells
                return True
        # v is not a valid value, reset cell back to 0
        mat[r][c] = 0

    # no suitable value found for this cell, previous cell values must change.
    return False


mat = board
if make_sk(mat):
    print("Congrats!! We have solved it.")
    pprint(mat, width=40, compact=True)
elif check_diagonal:
    print("Solution not found, trying with 'check_diagonal = False'.")
    check_diagonal = False
    if make_sk(mat):
        print("Congrats!! We have solved it.")
        pprint(mat, width=40, compact=True)
    else:
        print("Sorry, I am not able to solve this puzzle.")
else:
    print("Sorry, I am not able to solve this puzzle.")
    print("Sorry, I am not able to solve this puzzle.")
