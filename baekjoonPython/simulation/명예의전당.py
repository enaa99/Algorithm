
def solution(k, score):
    max_heap = []
    answer = []
    
    
    import heapq

    for sc in score:
        heapq.heappush(max_heap, sc)
        answer.append(min(heapq.nlargest(k, max_heap)))
    return answer

solution(3,[10,100,20,150,1,100,200])