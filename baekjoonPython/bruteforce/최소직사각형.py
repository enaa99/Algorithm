import sys

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]

def solution(sizes):
    big=[]
    small=[]
    for w,h in sizes:
        if w>h:
            big.append(w)
            small.append(h)
        else:
            big.append(h)
            small.append(w)
            
    return max(big)*max(small)