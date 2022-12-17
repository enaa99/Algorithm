import sys

l=[]
for i in range(9):
    l.append(int(sys.stdin.readline()))

tmp = sum(l) - 100
l.sort()
check = False
for i in range(9):
    if check:break
    for j in range(8):
        if l[i]+l[j+1] == tmp:
            l.pop(i)
            l.pop(j)
            # l.remove(l[i])
            # l.remove(l[j])
            check = True
            break
print(*l,sep='\n')


# pop()이 remove()보다 빠르다