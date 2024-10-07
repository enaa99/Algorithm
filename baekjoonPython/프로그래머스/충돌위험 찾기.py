
from collections import Counter
def solution(points, routes): 
    def min_route(route):
        # 경로를 저장할 path, 시간을 기록할 time
        path = []
        time = 0

        # 시작점과 도착점을 모두 탐색합니다.
        for i in range(len(route) - 1):
            # 시작점 sx, sy, 도착점 ex, ey
            sx, sy = points[route[i] - 1]
            ex, ey = points[route[i + 1] - 1]

            # x 좌표의 이동을 먼저 시작합니다.
            while sx != ex:
                # 시작점을 포함합니다.
                path.append((sx, sy, time))
                if sx > ex:
                    sx -= 1
                else:
                    sx += 1
                time += 1

            # y 좌표를 이동합니다.
            while sy != ey:
                # x 좌표가 이동이 끝났을 때 값을 추가합니다.
                path.append((sx, sy, time))
                if sy > ey:
                    sy -= 1
                else:
                    sy += 1
                time += 1

        # 최종적으로 도착점에 도착했을 때만 마지막으로 추가해줍니다.
        path.append((sx, sy, time))
        # 경로를 반환합니다.
        return path

    # 로봇의 모든 경로를 저장할 robot_routes
    robot_routes = []
    # 모든 지점을 이동합니다.
    for route in routes:
        # 각 경로를 robot_routes에 추가합니다.
        robot_routes.extend(min_route(route))

    # 충돌 지점의 개수 answer
    answer = 0
    # 로봇의 모든 경로의 겹치는 지점을 찾습니다.
    counter = Counter(robot_routes)
    # 반복문을 사용해 겹치는 지점이 있다면
    for v in counter.values():
        if v >= 2:
            # 충돌 지점을 증가시킵니다.
            answer += 1

    return answer