from collections import defaultdict
from itertools import combinations
def solution(pouches):
    max_jelly_sum = 0
    # 5가지 젤리
    # 최대한 많은 젤리 주머니
    # 어떤 한 가지 맛의 젤리 > 다른 모든 젤리의 합
    jelly_counts = []
    for pouch in pouches:
        counts = [0]*5
        for jelly in pouch:
            counts[ord(jelly) - 97] += 1
        jelly_counts.append(counts)
    
    def get_combi_sum(idx):
        total_counts = [0]*5
        for i in idx:
            for j in range(5):
                total_counts[i] += jelly_counts[j][i]
        return total_counts


    def is_valid(total_counts):
        max_value = max(total_counts)
        sum_value = sum(total_counts) - max_value
        return max_value >= sum_value

    for i in range(len(pouches), 0, -1):
        for idx in combinations(len(pouches), i):
            total_counts = get_combi_sum(idx)
            if is_valid(total_counts):
                return idx

    return 0