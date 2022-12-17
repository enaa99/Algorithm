import sys

input = sys.stdin.readline

mod = 1000000
fibo =[0,1]
n = int(input().strip())
p = mod//10*15
for i in range(2,p):
    fibo.append(fibo[i-1] + fibo[i-2])
    fibo[i] %= mod

print(fibo[n%p])