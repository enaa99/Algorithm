import sys
input = sys.stdin.readline

S = input().rstrip()
P = input().rstrip()

pa = [0]*len(P)

def pattern():
    j = 0
    for i in range(1,len(P)):
        while j>0 and P[i] !=P[j]:
            j = pa[j-1]
        if P[i] == P[j]:
            j +=1
            pa[i] = j

def KMP():
    j =0
    for i in range(len(S)):
        while j>0 and S[i] != P[j]:
            j = pa[j-1]
        if S[i] == P[j]:
            if j == len(P)-1:
                print(1)
                exit(0)
            else:
                j +=1
    print(0)
pattern()
KMP()