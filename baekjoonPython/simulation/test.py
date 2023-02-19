import random
import math

def is_prime(n, k=10):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    # n-1 = 2^s * d
    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    # Perform k rounds of Miller-Rabin test
    for _ in range(k):
        a = random.randint(2, n-2)
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            continue
        for _ in range(s-1):
            x = pow(x, 2, n)
            if x == n-1:
                break
        else:
            return False

    return True

def pollard_rho(n):
    if n == 1:
        return n
    if is_prime(n):
        return n

    # Miller-Rabin failed to prove n is prime, use Pollard's rho algorithm
    def f(x):
        return (x**2 + 1) % n

    x = y = random.randint(1, n-1)
    d = 1

    while d == 1:
        x = f(x)
        y = f(f(y))
        d = math.gcd(abs(x-y), n)
        if d == n:
            break

    return d

def factorize(n):
    factors = []
    while n > 1:
        factor = pollard_rho(n)
        factors.append(factor)
        n //= factor
    return factors


n = int(input())
factors = factorize(n)
for factor in factors:
    print(factor)
