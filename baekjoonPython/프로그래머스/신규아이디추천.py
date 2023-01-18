def solution(new_id):    
    allow =['a','b','c','d','e','f','g','h','i','j',
            'k','l','m','n','o','p','q','r','s','t',
            'u','x','y','z','w','v','1','2','3','4','5','6','7','8','9','0','-','_','.']
    
    new_id = new_id.lower()

    cnt = 0
    change = []
    for i in new_id:
        if i == '.': cnt+=1
        if i not in allow:
            change.append(i)
    
    for c in change:
        new_id = new_id.replace(c,'')
    
    for i in range(cnt,1,-1):
        new_id = new_id.replace('.'*i,'.')
    
    if new_id and new_id[0] == '.':
        new_id = new_id[1:]
    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]
    
    if len(new_id.strip()) == 0:
        new_id = 'a'
    
    if len(new_id) > 15:
        if new_id[14] == '.':
            new_id = new_id[:14]
        else:
            new_id = new_id[:15]
    
    elif len(new_id) <= 2:
        k = new_id[-1]
        while len(new_id) <= 2: 
            new_id += k
    
    
    return new_id


solution("abcdefghijklmn.p")