N = 'iㅜㅜbhazmhㅂ'
T = 6

key_dic = {'ㅂ':'q', 'ㅈ':'w','ㄷ':'e','ㄱ':'r','ㅅ':'t','ㅜ':'n'}

N = list(N)


start = 97
end = 123
answer = 0

for i in range(len(N)):
    
    if N[i] in key_dic:
        N[i] = key_dic[N[i]]
    
    k = ord(N[i])
    
    tmp = k-T
    
    if tmp < start:
        tmp = start-tmp
        answer = end - tmp
    else:
        answer = tmp
    
    N[i] = chr(answer)

print(*N)