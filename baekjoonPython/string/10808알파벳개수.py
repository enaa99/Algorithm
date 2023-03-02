import sys

input = sys.stdin.readline

arr = [0]*26

N = input().rstrip()

for i in N:
    arr[ord(i)-97] +=1

print(*arr, sep = ' ')
