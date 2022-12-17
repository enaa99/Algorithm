import sys
input = sys.stdin.readline

n = int(input())

memo = [0]*(n+1)

def fibo(n):
    if n == 0 or n == 1:
        return 1
    elif memo[n] !=0: return memo[n]
    
    else:
        memo[n] = fibo(n-2) + fibo(n-1)
        return memo[n]

print(fibo(n-1))
