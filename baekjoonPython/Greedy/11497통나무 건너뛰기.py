import sys 
input = sys.stdin.readline

for i in range(int(input())):
    X = int(input())
    nums = sorted(list(map(int, input().split())))
    level = 0
    for j in range(2, X):
        level = max(level, abs(nums[j] - nums[j - 2]))
    print(level)