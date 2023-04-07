def solution(S1, S2):
    

    # cache 딕셔너리 초기화
    cache = {}

    # DP로 이미지를 merge하며 black pixel 개수 계산
    for i in range(len(S1)):
        for j in range(len(S2)):
            # 이미지의 각 픽셀에 대해서 merge 결과 저장
            # (merge 결과는 다시 계산하지 않도록 cache 딕셔너리에 저장)
            if S1[i] == "b" and S2[j] == "b":
                cache[(i, j)] = 1
            else:
                cache[(i, j)] = 0

    # 계산된 결과를 이용하여 black pixel 개수 반환
    return 1024 - sum(cache.values())

print(solution('b', 'w'))

print(solution('ppwwwbpbbwwbw', 'pwbwpwwbw')) # 640 출력
print(solution('b', 'w')) # 1024 출력
