import sys

input = sys.stdin.readline

# 테스트 케이스 T
T = int(input())

def Post(root,start,end):
    for i in range(start,end):
        if ino[i] == pre[root]:
            Post(root+1,start,i) # left subtree
            Post(root+i+1-start,i+1,end) # right subtree
            print(pre[root],end=" ")



for _ in range(T):
    n = int(input()) # 노드개수 
    pre = list(map(int,input().split()))
    ino = list(map(int,input().split()))
    Post(0,0,n)
    print()