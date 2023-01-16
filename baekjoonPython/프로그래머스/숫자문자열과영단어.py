def solution(s):    
    alpha_dic ={'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    
    
    for key in alpha_dic.keys():
        if key in s:
            s = s.replace(key,alpha_dic[key])
    
    
    return int(s)