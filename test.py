n = int(input())  # 벽의 개수 n 입력받기

# n번째 좌측 벽을 이루는 육각형의 번호 구하기
if n == 1:
    left = 1
else:
    left = n * (n-1) + 1

# n번째 우측 벽을 이루는 육각형의 번호 구하기
if n == 1:
    right_top = 1
    right_bottom = 1
else:
    right_top = left - n + 1
    right_bottom = left + 2*n - 2

# 나머지 육각형의 번호 구하기
left_bottom = left + 3*n - 3
left_top = left + 4*n - 4
center = left + 5*n - 5

# 출력하기
print(left, right_top, right_bottom, left_bottom, left_top, right, center)
