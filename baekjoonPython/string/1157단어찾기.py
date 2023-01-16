s = input().rstrip()

s_dict = {}
tmp = 0
for i in s:
    i = i.upper()
    if i not in s_dict:
        s_dict[i] = 0
    else:
        s_dict[i] +=1
        tmp = max(tmp,s_dict[i])


cnt = 0
for i in s_dict.values():
    if i == tmp:
        cnt +=1

if cnt > 1:
    print('?')
else:
    for i in s_dict.keys():
        if s_dict[i] == tmp:
            print(i)
            break