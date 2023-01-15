def solution(k, m, score):
    import heapq
    apples = []
    for apple in score:
        heapq.heappush(apples,-apple)
    cnt = len(score)//m
    
    answer = [[]for _ in range(cnt)]
    j = 0
    while len(apples) >= m:
        for _ in range(m):
            answer[j].append(-heapq.heappop(apples))
        j +=1
    ans = 0
    for apple in answer:
        tmp = 0
        tmp += min(apple)
        ans += tmp*m
    
    return ans

solution(3,4,[1,2,3,1,2,3,1])