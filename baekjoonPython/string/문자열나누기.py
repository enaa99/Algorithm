def solution(s):
    answer = 0
    from collections import deque
    
    q= []
    s= deque(s)
    ans = [0]*2
    while s:
        v = s.popleft()
        if not q:
            ans[0] += 1
            q.append(v)
        else:            
            if q[0] == v:
                ans[0] +=1
                q.append(v)
            else:
                ans[1] += 1
                q.append(v)
                
                if ans[0] == ans[1]:
                    q.clear()
                    ans =[0]*2
                    continue
            # else:
            #     v = s.popleft()
            #     ans[ord(v)-97] +=1 
            #     q.append(v)
    if q:
        answer +=1

    return answer

solution("aaabbaccccabba")