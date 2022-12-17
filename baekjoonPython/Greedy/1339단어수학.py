import sys
input = sys.stdin.readline

n = int(input())

l = [input().rstrip() for _ in range(n)] 

l_dict = {} 

numList = [] 


for i in range(n): 
    for j in range(len(l[i])): 
        if l[i][j] in l_dict:
            l_dict[l[i][j]] += 10 ** (len(l[i])-j-1)
        else:   
            l_dict[l[i][j]] = 10 ** (len(l[i])-j-1)

for val in l_dict.values(): 
    numList.append(val)

numList.sort(reverse=True) 

sum = 0
pows = 9
for i in numList: 
    sum += pows * i
    pows -= 1

print(sum)