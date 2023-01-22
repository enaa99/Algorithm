def solution(arrayA,arrayB):
    answer = 0
    
    min_a = min(arrayA)
    min_b = min(arrayB)
    
    
    def find(k):
        arr = [k]
        for i in range(2,int(k**0.5)+1):
            if k%i == 0:
                arr.append(i)
                arr.append(k//i)
        return arr
    
    def max_value(k,cmp1,cmp2):
        for k in cmp1:
            if k%i != 0:
                return False
        for k in cmp2:
            if k%i == 0:
                return False
        return True

    a = find(min_a)
    b = find(min_b)
    answer = 0
    
    a.sort(reverse=True)
    b.sort(reverse=True)
    
    
    for i in a:
        if max_value(i,arrayA,arrayB):
            answer = i
            break
    for i in b:
        if max_value(i,arrayB,arrayA):
            answer = max(answer,i)
            break
    
    
    return answer

solution([10,20],[5,17])