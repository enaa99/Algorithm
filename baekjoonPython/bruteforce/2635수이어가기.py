import sys

input = sys.stdin.readline

first_num = int(input())

len_result = 0
result = []

for i in range(first_num+1):
    result_list = [first_num, i]
    j = 0
    while True:
        last_num = result_list[j] - result_list[j+1]
        j += 1
        if last_num < 0:
            break
        result_list.append(last_num)
        if len_result < len(result_list):
            len_result = len(result_list)
            result = result_list[:]

print(len_result)
print(*result)