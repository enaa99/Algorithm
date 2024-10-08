from collections import defaultdict
def solution(points, routes):
    answer = 0
    
    way = defaultdict(int)
    
    #move x
    def move_x(x,y,count):
        a, b = points[x-1][:], points[y-1]
        
        while a[0] != b[0]:
            if a[0] < b[0]:
                a[0] += 1
            else:
                a[0] -= 1 
            count +=1
            way[f"{a[0]},{a[1]},{count}"] += 1
        return count
    
    def move_y(x,y, count):    
        a, b = points[x-1][:], points[y-1]
                
        while a[1] != b[1]:
            if a[1] < b[1]:
                a[1] += 1
            else:
                a[1] -= 1
            count +=1    
            way[f"{b[0]},{a[1]},{count}"] += 1
        return count
    
    for route in routes:
        count = 0
        way[f"{points[route[0]-1][0]},{points[route[0]-1][1]},0"] += 1
        for i in range(len(route)-1):
            count = move_x(route[i],route[i+1], count)
            count =move_y(route[i],route[i+1], count)
        
    for i in way.values():
        if i > 1:
            answer +=1
    
            
    return answer


# solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [4, 2], [4, 3]])
solution([[2, 2], [2, 3], [2, 7], [6, 6], [5, 2]], [[2, 3, 4, 5], [1, 3, 4, 5]])