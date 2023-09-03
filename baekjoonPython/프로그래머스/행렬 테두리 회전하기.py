import heapq


def solution(rows, columns, queries):
    answer = []

    graph = [[k+1+(columns*i) for k in range(columns)] for i in range(rows)]


    for y1,x1,y2,x2 in queries:
        heap = []

        y1x1 = graph[y1-1][x1-1]
        y1x2 = graph[y1-1][x2-1]
        y2x1 = graph[y2-1][x1-1]
        y2x2 = graph[y2-1][x2-1]

        heapq.heappush(heap,y1x1)
        heapq.heappush(heap,y1x2)
        heapq.heappush(heap,y2x1)
        heapq.heappush(heap,y2x2)

        for x in range(x2 - 1, x1 - 1, -1):
            graph[y1-1][x] = graph[y1-1][x-1]
            heapq.heappush(heap, graph[y1-1][x])

        for y in range(y2 - 1, y1 - 1, -1):
            graph[y][x2-1] = graph[y-1][x2-1]
            heapq.heappush(heap, graph[y][x2-1])

        for x in range(x1 - 1, x2 - 1, 1):
            graph[y2-1][x] = graph[y2-1][x+1]
            heapq.heappush(heap, graph[y2-1][x])

        for y in range(y1 - 1, y2 - 1, 1):
            graph[y][x1-1] = graph[y+1][x1-1]
            heapq.heappush(heap, graph[y][x1-1])

        graph[y1][x2-1] = y1x2
        graph[y2-1][x2-2] = y2x2
        graph[y2-2][x1-1] = y2x1

        answer.append(heap[0])

    return answer


solution(100,97,[[1,1,100,97]])