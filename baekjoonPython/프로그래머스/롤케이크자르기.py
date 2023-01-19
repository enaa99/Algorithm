from collections import Counter
def solution(topping):
    answer = 0
    me = {}
    # me = Counter(topping)
    for i in topping:
        # i = str(i)
        if i in me:
            me[i] += 1
        else:
            me[i] = 1
    
    bro = {}
    
    for i in range(len(topping)) :
        if topping[i] in bro :
            bro[topping[i]] += 1
        else :
            bro[topping[i]] = 1
        me[topping[i]] -= 1
        
        if me[topping[i]] == 0 :
            del me[topping[i]]
        
        if len(bro) == len(me) :
            answer +=1
    
    return answer


solution([1,2,1,3,1,4,1,2])