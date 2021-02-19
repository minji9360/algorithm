N, M = map(int, input().split())
x, y, d = map(int, input().split())
count = 1
loopCnt = 0
gameMap = []
direction = [0, 1, 2, 3]
movement = [[-1, 0], [0, 1], [1, 0], [0, -1]] # 0, 1, 2, 3 방향으로 전진할 때 위치값
currentPosition = [x, y]

for i in range(N):
    gameMap.append(list(input().split()))

while 1:
    nextPosition = [currentPosition[0] + movement[d - 1][0], currentPosition[1] + movement[d - 1][1]]
    if gameMap[nextPosition[0]][nextPosition[1]] == '0':
        d = direction[d - 1]
        currentPosition = nextPosition
        count += 1
        loopCnt = 0
        gameMap[currentPosition[0]][currentPosition[1]] = 1
    else:
        if loopCnt == 4:
            break
        d = direction[d - 1]
        loopCnt += 1

print(count)

