from collections import Counter
from collections import defaultdict

def solution(want,number,discount):
    answer = 0
    
    check = defaultdict(int)
    check = Counter(discount[:10])
    
    buy = {}
    
    for i in range(len(want)):
        buy[want[i]] = number[i]
    
    
    
    
    def cmp(arr1,arr2):
        for key in arr1.keys():
            if arr1[key] > arr2[key]:
                return False
        return True
    
    if cmp(buy,check):
        answer +=1 
    
    for i in range(10,len(discount)):
        check[discount[i]] += 1
        check[discount[i-10]] -= 1
        
        if cmp(buy,check):
            answer +=1
        
    
    
    return answer


solution(['banana','apple','rice','pork','pot'],[3,2,2,2,1],
        ["chicken", "apple", "apple", "banana", "rice", "apple",
        "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"])