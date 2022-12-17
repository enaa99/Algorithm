import sys

input = sys.stdin.readline

###### 큐
class Node:
    def __init__(self,data) :
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
    def add(self,node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
    def poll(self):
        if self.head == None:
            return False
        
        tmp = self.head.next
        self.head.data = None
        self.head.next = None
        self.head = tmp

        if self.head.next == None:
            self.tail = self.head
        
    def search(self,data):
        if self.head == None:
            return False
        
        tmp = self.head
        while tmp.next != None:
            v = tmp.data
            if data == v:
                return True
            tmp = tmp.next
######


#보드크기
N = int(input())
l = [[0 for _ in range(N)]for m in range(N)]

#사과개수만큼 리스트의 0값을 1로 변경
for _ in range(int(input())):
    a,b = map(int,input().split())
    l[a-1][b-1] = 1
    

# 방향 변환 횟수
c = int(input())
change = []
for _ in range(c):
    t,w = map(str,input().split())
    change.append((int(t),w))

q = LinkedQueue()

dx =[0,1,0,-1]
dy =[1,0,-1,0]
time = 0

def checkTime():
    global time
    global direction
    if time >= len(change): return
    if cnt == change[time][0]:
        if change[time][1] == 'D':
            direction = (direction+1)%4
        else:
            direction = (direction-1)%4
        time +=1
snake = []
cnt =0
direction = 0
x,y = 0,0
snake.append((0,0))
while True:
        cnt += 1
        x += dx[direction]
        y += dy[direction] 
        
        if x < 0 or x>=N or y < 0 or y>=N:
            break
        
        if l[x][y] == 1:
            l[x][y] = 0
            
            snake.append((x,y))
        else :
            if (x,y) in snake:
                break
            if snake:
                snake.pop(0)
            snake.append((x,y))
        
        
        checkTime()
        
print(cnt)