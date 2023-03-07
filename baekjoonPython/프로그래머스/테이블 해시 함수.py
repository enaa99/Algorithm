def solution(data,col,row_begin,row_end):
    answer =0 
    
    # col 값에 따라 오름차순 정렬
    
    data.sort(key =lambda x:(x[col-1],-x[0]))
    
    tmp = []
    for num in range(row_begin-1,row_end):
        k = 0
        for j in data[num]:
            k += j%(num+1)
        tmp.append(k)
    
    answer = tmp[0]
    for i in range(1,len(tmp)):
        answer = answer^tmp[i] 
    
    
    return answer



solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]],2,2,3)