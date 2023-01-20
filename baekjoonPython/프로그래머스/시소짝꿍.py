from collections import defaultdict

def solution(weights):
    answer = 0
    dict1 = defaultdict(int)
    w_dict = defaultdict(int)

    for i in weights:
        tmp = dict1[i*2] + dict1[i*3] + dict1[i*4]
        if tmp != 0 and i in w_dict:
            tmp -= 2 * w_dict[i]
        for j in range(2,5):
            dict1[i*j] += 1
        w_dict[i] += 1
        answer += tmp
    return answer


solution([100,180,360,100,270])