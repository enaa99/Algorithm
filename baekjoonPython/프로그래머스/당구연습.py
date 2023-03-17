import sys
def solution(m, n, startX, startY, balls):
    answer = []
    for x,y in balls:
        answer.append(make_target(startX, startY, x,y,m,n))
    return answer

def make_target(startX, startY, targetX, targetY, m,n):
    distance=sys.maxsize
    if not (startY==targetY and startX>targetX):
        distance = min(distance,(startX+targetX)**2+abs(startY-targetY)**2)
    if not (startX==targetX and startY>targetY):
        distance = min(distance, abs(startX-targetX)**2 + (startY+targetY)**2)
    if not (startY==targetY and startX<targetX):
        distance = min(distance, ((m-startX)+(m-targetX))**2 + abs(startY-targetY)**2)
    if not (startX==targetX and startY<targetY):
        distance = min(distance,((n-startY)+(n-targetY))**2 + abs(startX-targetX)**2)

    return distance