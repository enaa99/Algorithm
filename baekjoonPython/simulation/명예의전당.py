
def solution(k, score):
    max_heap = []
    answer = []
    
    import heapq

    for sc in score:
        heapq.heappush(max_heap, (-sc, sc))
        answer.append(max(heapq.nsmallest(k, max_heap))[1])
    return answer

solution(3,[10,100,20,150,1,100,200])