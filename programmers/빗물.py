# 빗물 투포인터 !!

def solution(bricks):
    answer = 0
    left, right = 0, len(bricks) - 1
    max_left, max_right = bricks[left], bricks[right]

    while left < right:
        max_left, max_right = max(max_left, bricks[left]), max(max_right, bricks[right])
        if max_left <= max_right:
            answer += max_left - bricks[left]
            left += 1
        else:
            answer += max_right - bricks[right]
            right -= 1
    return answer


solution([0,2,0,1,3,1,2,0,1,0,2,0])