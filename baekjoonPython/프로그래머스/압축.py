from collections import defaultdict,deque
def solution(msg):
    answer = []
    
    tmp = defaultdict(int)
    
    msg = deque(msg)
    
    for i in range(26):
        tmp[chr(i+65)] = i+1
    
    cnt = 27
    while msg:
        v = msg.popleft()
        
        while msg and tmp[v+msg[0]]:
            v += msg.popleft()
        
        answer.append(tmp[v])
        
        if msg:
            v += msg[0]
            tmp[v] = cnt
            cnt +=1
    return answer

solution('KAKAO')


