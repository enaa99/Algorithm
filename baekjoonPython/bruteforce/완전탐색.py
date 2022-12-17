import sys
    
answers = [1,2,3,4,5]

answer = []
check =[0,0,0]

a = [1,2,3,4,5]
b = [2,1,2,3,2,4,2,5]
c = [3,3,1,1,2,2,4,4,5,5]

for i in range(len(answers)):
    if a[i%5] == answers[i]:
        check[0] += 1
    if b[i%8] == answers[i]:
        check[1] += 1
    if c[i%10] == answers[i]:
        check[2] += 1
for i in check:
    if not answer:
        answer.append(i)
    else:
        while answer[-1] < i:
            answer.pop()
            if not answer: break
        answer.append(i)
        
