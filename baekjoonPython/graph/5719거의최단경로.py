import sys
import heapq

input = sys.stdin.readline



# N 장소의 수 , 도로의 수 M
# 시작점 S , 도착점 D
# U,V,P U에서 V로 가는 비용 P

# 0,S

def BFS(min_v):
    q = []
    q.append([0,D])

    while q:
        cur_value,cur_road = heapq.heappop(q)
        
        for next_value,next_road in loads_reverse[cur_road]:
            next_val = cur_value+next_value
            if next_val+distance[next_road] == min_v:
                if not way_check[next_road][cur_road]:
                    way_check[next_road][cur_road] = True
                    q.append((next_val,next_road))
    

def djikstra():
    q =[]
    distance[S] = 0
    q.append([0,S])
    isVisited =[0]*N
    # ans = set()
    while q:
        value,way = heapq.heappop(q)
        if way == D:
            return value
        
        if distance[way] < value: continue
        if isVisited[way]: continue
        isVisited[way] = 1
        
        for next_value,road in loads[way]:
            next_dist =  distance[way] + next_value
            if distance[road] >= next_dist and not way_check[way][road]: 
                distance[road] = next_dist
                heapq.heappush(q, [next_dist,road])
            # heapq.heappush(q,[value+next_value,road])


while True:

    N,M = map(int,input().split())
    
    if N == M == 0:
        exit(0)
    
    S,D = map(int,input().split())
    
    loads = [[]for _ in range(N)]
    way_check=[[False]*N for _ in range(N)]
    loads_reverse = [[]for _ in range(N)]
    
    for i in range(M):
        u,v,p = map(int,input().split())
        loads[u].append([p,v])
        loads_reverse[v].append([p,u])
    distance =[sys.maxsize]*N
    min_val = djikstra()
    if min_val == None:
        print(-1)
        continue
    BFS(min_val)
    distance =[sys.maxsize]*N
    k = djikstra()
    print(k if k!=None else -1)
