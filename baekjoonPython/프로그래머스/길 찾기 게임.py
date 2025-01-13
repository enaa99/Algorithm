from collections import defaultdict

def solution(nodeinfo):
    answer = [[]]
    
    node_dic = defaultdict(int)
    
    # y값이 가장 높은게 root
    # x 값에 따라 좌 우 구분
    
    graph = [[] for _ in range(len(nodeinfo))]
    
    for i in range(len(nodeinfo)):
        node_dic[f"{nodeinfo[i][0]},{nodeinfo[i][1]}"] = i
    
    nodeinfo.sort(key=lambda x:(-x[1],x[0]))
    
    node_graph = []
    
    k = 6
    
    
    for i ,(k,v) in enumerate(nodeinfo):
        is_append = False
        for j,(a) in enumerate(node_graph):
            if int(a[0].split(',')[1]) == v:
                is_append = True
                node_graph[j].append(f"{k},{v}")
            
        if not is_append:
            node_graph.append([f"{k},{v}"])

    print(node_graph)
    
    return answer

solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]])