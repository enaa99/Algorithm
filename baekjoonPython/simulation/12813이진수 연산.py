import sys

input = sys.stdin.readline

# 1 A&B , A|B , A^B , ~A, ~B



A = str(input().rstrip())

B = str(input().rstrip())


for i in range(len(A)):
    print(int(A[i]) & int(B[i]),end='')
print()
for i in range(len(A)):
    print(int(A[i]) | int(B[i]),end='')
print()
for i in range(len(A)):
    print(int(A[i]) ^ int(B[i]),end='')
print()
for i in range(len(A)):
    if A[i] == '0':
        print(1,end='')
    else:
        print(0,end='')
print()
for i in range(len(A)):
    if B[i] == '0':
        print(1,end='')
    else:
        print(0,end='')
