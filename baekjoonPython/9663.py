import sys

n = int(sys.stdin.readline())
sum = 0
l = [0] * n


def checking(k):
    for i in range(k):
        if l[k] == l[i] or (abs(l[k]-l[i]) == abs(k-i)):
            return False
    return True


def queen(k):
    global sum
    if k == n:
        sum += 1
        return
    else:
        for i in range(n):
            l[k] = i
            if checking(k):
                queen(k+1)

# queen(0)
# print(sum)
