import math

def lcm(a, b):
    return int( a * b / math.gcd(a, b))

def solution(arr):
    answer = 0

    stk = []

    for el in arr:
        if not stk:
            stk.append(el)
        else:
            stk.append(lcm(stk.pop(), el))

    return stk[-1]