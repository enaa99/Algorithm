import sys


w,h = map(int,sys.stdin.readline().split())

width =[0,w]
height = [0,h]

for i in range(int(sys.stdin.readline())):
    a,b = map(int,sys.stdin.readline().split())
    if(a == 0):
        height.append(b)
    else:
        width.append(b)
height.sort()
width.sort()

h = 0
w = 0

for i in range(1,len(height)):
    h = max(h,height[i]-height[i-1])
for i in range(1,len(width)):
    w = max(w,width[i]-width[i-1])

print(h*w)