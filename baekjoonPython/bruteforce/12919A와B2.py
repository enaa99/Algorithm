
s = input()
t = input()

def find(t):
    if len(t)==len(s):
        return t==s
    if t[0] == 'B' and find(t[:0:-1]): #뒤집이서 0번째 빼고 출력 
        return True
    if t[-1] == 'A' and find(t[:-1]): #추가한 A빼고 
        return True
    
print(1 if find(t) else 0)