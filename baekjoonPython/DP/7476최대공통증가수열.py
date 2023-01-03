import sys

input = sys.stdin.readline

# 수열의 길이 M
M = int(input())

number_1 = list(map(int,input().split()))

N = int(input())

number_2 = list(map(int,input().split()))


len_1 = len(number_1)
len_2 = len(number_2)

number_dic = {}
number = []
flag = 0

def index_num(k,arr,check):
    tmp = []
    for i in range(len(arr)):
        if k == arr[i] and i not in check:
            tmp.append(i)
    return tmp

if len_1 > len_2:
    for i in range(len(number_2)):
        if number_2[i] in number_1 and number_dic.get(f'{number_2[i]}') == None:
            k = index_num(number_2[i],number_1,number_dic)
            if k :
                number.append(number_2[i])
                number_dic[f'{number_2[i]}']= k
    flag = 1
else:
    for i in range(len(number_1)):
        if number_1[i] in number_2 and number_dic.get(f'{number_1[i]}') == None:
            k = index_num(number_1[i],number_2,number_dic)
            if k :
                number.append(number_1[i])
                number_dic[f'{number_1[i]}'] = k

if not number:
    print(0)
    exit(0)


dp =[[1]*len(number_dic[f'{number[_]}']) for _ in range(len(number))]

cnt = 0
# if flag:
#     for i in range(1,len(number)):
#         for j in range(i-1,-1,-1):
#             if number[i] > number[j] :
#                 for l in number_dic[f'{number[i]}']:
#                     for k in number_dic[f'{number[j]}']:
#                         if l > k dp:
                            
            
            
        # if number.get(f'{number_2[i]}') and number.get(f'{number_2[j]}') 
        # if number.get(f'{number_2[num]}'):
        #     for i in number[f'{number_2[num]}']:
                
            


# else:
#     for i in range(1,len(number)):
#         for j in range(i-1,-1,-1):
#             if number[i] > number[j] and dp[i] <= dp[j] and number_2[number[i]] > number_2[number[j]]:
#                 dp[i] = dp[j] + 1
    
#     max_value = max(dp)
    
#     print(max_value)
#     q = []
#     for num in range(len(dp)-1,-1,-1):
#         if dp[num] == max_value:
#             if q:
#                 if q[-1] > number_2[number[num]]:
#                     max_value -= 1
#                     q.append(number_2[number[num]])
#             else:
#                     max_value -= 1
#                     q.append(number_2[number[num]])
#         if max_value == 0:
#             break
#     print(*q[::-1])


