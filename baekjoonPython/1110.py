from msvcrt import kbhit
import sys

k = int(sys.stdin.readline())  
ans = k           
count = 0         
while True:
    x = ans//10
    y = ans %10
    z = (x+y)%10
    ans = (y*10) + z
    count += 1
    
    if(ans == k):break
 
print(count)