n, l = map(int, input().split())
names = [input().strip() for _ in range(n)]

for i in range(l):
    for j in range(26):
        tmp = chr(ord('A') + j)
        flag = True
        for name in names:
            cnt = 0
            for k in range(l):
                if k == i:
                    if name[k] != tmp:
                        cnt += 1
                else:
                    if name[k] != names[0][k]:
                        cnt += 1
            if cnt > 1:
                flag = False
                break
        if flag:
            print(names[0][:i] + tmp + names[0][i+1:])
            exit()
print("CALL FRIEND")
