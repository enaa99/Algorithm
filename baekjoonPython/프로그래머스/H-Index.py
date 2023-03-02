def solution(citations):
    
    
    
    citations.sort()
    len_k = len(citations)
    for i in range(len_k):
        if citations[i] >= len_k -i:
            return citations[i]
    
    