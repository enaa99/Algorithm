import sys

input = sys.stdin.readline

# X,A,B,C,D

X,a,b,c,d = map(int,input().split())




# 동전의 개수 최대로
# a -> 1 / b -> 5 / c -> 10 / d -> 25


dp = [[0]*4 for _ in range(10001)]


for i in range(X):
    for j in range(4):
        dp[i][j] = 
