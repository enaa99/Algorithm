import sys

input = sys.stdin.readline

N = int(input())

move = list(map(str,input().rstrip()))


graph = [['.']*N for _ in range(N)]
m_vertical = False

def r_move(x,y,k):
    global m_vertical
    
    if k == 'U':
        x -= 1
        m_vertical = True
    elif k == 'D':
        x += 1
        m_vertical = True

    elif k == 'R':
        y += 1
        m_vertical = False
    else:
        y -= 1
        m_vertical = False
    return x,y


def paint_graph(m,n):
    if graph[m][n] == '+': return
    
    if m_vertical:
        if graph[m][n] == '.':
            graph[m][n] ='|'
        elif graph[m][n] == '-':
            graph[m][n] = '+'
    else:
        if graph[m][n] =='.':
            graph[m][n] = '-'
        elif graph[m][n] =='|':
            graph[m][n] = '+'


def robot_move(a,b):
    x,y = a,b
    for dir in move:
        xa,ya = x,y        
        x,y = r_move(x,y,dir)
        if x<0 or y <0 or x>=N or y>=N :
            x,y = xa,ya 
            continue
        
        paint_graph(xa,ya)
        paint_graph(x,y)
        

robot_move(0,0)

for i in range(N):
    print(*graph[i], sep="")