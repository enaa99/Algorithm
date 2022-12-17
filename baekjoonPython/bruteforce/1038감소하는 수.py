import sys
from itertools import combinations

n = int(sys.stdin.readline())

nums = list()         # 모든 감소하는 수
for i in range(1,11): # 1~10 개의 조합 만들기 
    for comb in combinations(range(0,10),i): # 0~9로 하나씩 조합 만들기
        comb = list(comb)
        comb.sort(reverse=True)
        nums.append(int("".join(map(str,comb))))

nums.sort() #오름차순
try:
    print(nums[n])
except:
    print(-1)