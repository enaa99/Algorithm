import sys

input = sys.stdin.readline

N = int(input())

numbers = list(map(str,input().rstrip()))


ans = 0


for num in numbers:
    ans += int(num)


print(ans)