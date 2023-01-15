












def solution(X, Y):
    answer = ''

    x = {str(i):0 for i in range(10)}
    y = {str(i):0 for i in range(10)}

    
    for i in X:
        x[i] += 1
    for i in Y:
        y[i] += 1
    
    for i in range(9,-1,-1):
            i = str(i)
            k = min(x[i],y[i])
            
            if answer == ''and i =='0' and k !=0:
                return '0'
            answer = ''.join([answer,i*k])
            
    if answer == '':
        return '-1'
    else:
        return answer

    # x = {i:0 for i in X}
    # y = {i:0 for i in Y}
    

    
    # for i in X:
    #     x[i] += 1
    # for i in Y:
    #     y[i] += 1
    
    # for i in range(9,-1,-1):
    #     if x[i] != 0 and y[i] != 0:
    #         k = min(x[i],y[i])
    #         if k == 0:
    #             answer += str(i)*k
    #         else:
    #             answer += str(i)*k
    # if answer:
    #     answer = int(answer)
    # else:
    #     answer = '-1'
    # return str(answer)
    

solution("5525", "1255")