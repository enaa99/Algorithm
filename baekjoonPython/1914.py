# import sys


# n = int(sys.stdin.readline())

# arr = []

# def Hanoi(k,start,mid,end):
#     if k == 1:
#         # k == 1이라면 a에서 c로 한번만 옮기면 끝!
#         print(start,end)
#         return
#     Hanoi(k-1,start,end,mid)
#     Hanoi(1,start,mid,end)
#     Hanoi(k-1,mid,start,end)



# print(2**n-1)
# if n < 20:
#     Hanoi(n,1,2,3)

def solution(n):
    answer = []
    
    def hanoi(k,start,mid,end):
        if k == 1:
            answer.append([start,end])
            return
        
        hanoi(k-1,start,end,mid)
        hanoi(k-1,start,mid,end)
        hanoi(k-1,mid,start,end)
    
    
    hanoi(n,1,2,3)
    
    return answer
solution(2)