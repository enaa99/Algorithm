from collections import defaultdict

def solutioin(record):
    answer = []
    
    
    # uid 로만 구분
    # case Enter, Prodo, Change
    
    name_dic = defaultdict(str)
    q = []
    for recording in record:
        splits = recording.split()
        
        if splits[0] != 'Leave':
            name_dic[splits[1]] = splits[2]
        
        q.append([splits[1],splits[0]])
    
    
    for name,state in q:
        if state == 'Enter':
            answer.append(f"{name_dic[name]}님이 들어왔습니다.")
        elif state == 'Leave':
            answer.append(f"{name_dic[name]}님이 나갔습니다.")

    
    
    
    
    
    
    
    
    
    return answer