
    
def solution(users, emoticons:list):
    answer = [0,0]
    discount = []
    data = [10,20,30,40]
    
    def dfs(temp,depth):
        if len(temp) == depth:
            discount.append(temp[:])
            return
    
        for d in data:
            temp[depth] += d
            dfs(temp,depth+1)
            temp[depth] -= d
    
    dfs([0]*len(emoticons),0)
    
    for d in range(len(discount)):
        join , price = 0,[0]*len(users)
        for e in range(len(emoticons)):
            for u in range(len(users)):
                if discount[d][e] >= users[u][0]:
                    pass
    
    
    return answer


solution([[40, 10000],[25, 10000]],[7000, 9000])