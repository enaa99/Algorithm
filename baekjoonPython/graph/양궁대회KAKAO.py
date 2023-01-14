def solution(n, info):
    from collections import deque
    
    def BFS():
        q= deque()
        rion_arr = [0]*11
        q.append([0,rion_arr])
        max_gap = 0
        ans = []
        
        while q:
            depth, arr = q.popleft()
            
            if sum(arr) == n:
                apeach, rion = 0,0
                for i in range(11):
                    if arr[i] == info[i] == 0: continue
                    elif arr[i] <= info[i]:
                        apeach += 10 - i
                    else:
                        rion += 10 - i
                if rion > apeach:
                    gap = rion - apeach
                    if max_gap > gap: continue
                    if max_gap < gap:
                        ans.clear()
                        max_gap = gap
                    ans.append(arr[:])
                    
            elif sum(arr) > n: continue
            
            elif depth == 11:
                arr[depth-1] += n - sum(arr)
                q.append([-1,arr[:]])
            else:
                rion_shot = arr[:]
                rion_shot[depth] += info[depth] + 1
                q.append([depth+1,rion_shot])
                q.append([depth+1,arr[:]])
        return ans
    
    rion = BFS()
    
    if not rion:
        return [-1]
    else:
        return rion[-1]
    
