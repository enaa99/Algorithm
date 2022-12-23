import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = [list(map(int,input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]


