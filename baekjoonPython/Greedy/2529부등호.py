import sys

input = sys.stdin.readline

N = int(input())

cmp = list(map(str,input().split()))
len_cmp = len(cmp)

arr = [0]*(len_cmp+1)
isUsed = [0]*10

def check(idx):
    if idx == 0: return True
    else:
        if cmp[idx-1] == '>':
            if int(arr[idx-1]) > int(arr[idx]):
                return True
        else:
            if int(arr[idx-1]) < int(arr[idx]):
                return True
    return False
        
        

def dfs(depth,start,end,sum):
    if depth == len_cmp+1:
        return True    
    
    for i in range(start,end,sum):
        if not isUsed[i]:
            isUsed[i] = 1
            arr[depth] = str(i)
            if check(depth):
                if dfs(depth+1,start,end,sum):
                    return True
                isUsed[i] = 0
            else:
                isUsed[i] = 0
                return False
    return False


dfs(0,0,10,1)
min_v = ''.join(arr)

arr = [0]*(len_cmp+1)
isUsed = [0]*10
dfs(0,9,-1,-1)
max_v = ''.join(arr)

print(max_v)
print(min_v)
