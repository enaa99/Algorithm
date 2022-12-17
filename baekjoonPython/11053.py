import sys

input = sys.stdin.readline

n = int(input())
l = list(map(int,input().split()))
k =[0]*n

for i in range(n):
	for j in range(0, i):
		if (l[j] < l[i] and k[i] < k[j]+1):
			k[i] = k[j] + 1

print(max(k)+1)