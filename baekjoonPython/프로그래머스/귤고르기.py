from collections import defaultdict
from collections import Counter
def solution(k,tangerine):
    answer = 0
    
    guel = defaultdict(int)
    
    temp = Counter(tangerine)
    
    
    for i in tangerine:
        guel[i] += 1
    
    tmp = []
    for i in guel.values():
        tmp.append(i)
    
    tmp.sort(reverse=True)
    
    
    for i in tmp:
        if k <= 0:
            break
        answer +=1
        k -= i
    
    return answer


solution(6,[1,3,3,3,2,5,4,5,2,3,6])