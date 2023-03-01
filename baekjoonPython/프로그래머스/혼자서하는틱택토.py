
def check_win(p, b):
    for i in range(3):
        if all(cell == p for cell in b[i]):
            return True
    for j in range(3):
        if all(b[i][j] == p for i in range(3)):
            return True
    if all(b[i][i] == p for i in range(3)):
        return True
    if all(b[i][2-i] == p for i in range(3)):
        return True

    return False

def solution(b):
    X = sum(row.count('X') for row in b)
    O = sum(row.count('O') for row in b)

    if X - O > 0 or abs(X - O) > 1:
        return 0
    elif (check_win('O', b) and check_win('X', b)):
        return 0
    elif (check_win('O', b) and X != O - 1) or (check_win('X', b) and X != O):
        return 0
    return 1