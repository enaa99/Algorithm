import sys
l = []
for _ in range(int(sys.stdin.readline())):
    l.append(sys.stdin.readline().split('\n')[0])

l =set(l)
l = sorted(l,key=lambda x:(len(x),x))
for i in l:
    print(i)


# 중복제거
# 1. set(list)
# 2. comprehension
# 3. for loop
# 4. dic.fromkeys() dic 키 추출