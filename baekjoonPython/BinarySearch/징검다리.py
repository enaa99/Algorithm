import sys

input = sys.stdin.readline

def solution(distance,rocks:list,n):
    rocks.sort()
    
    l = 0
    r = distance +1
    
    while l+1 < r:
        mid = (l+r)//2
        
        del_stones = 0
        pre_stone = 0
        
        for rock in rocks:
            if rock - pre_stone < mid:
                del_stones += 1
            else:
                pre_stone = rock
            if del_stones > n: break
        
        if del_stones > n: r = mid
        else:
            l = mid
    
    return l

rocks = [2, 14, 11, 21, 17]
solution(25,rocks,2)