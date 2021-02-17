import sys
N = int(input())
days = []
for i in range(N):
    days += [list(map(int, sys.stdin.readline().split()))]
    # 2차원 배열을 입력받을 때, 그냥 days += [sys....] 하면 string 타입으로 입력받게 됨
    # int 타입으로 입력받고 싶을 때는 위와 같은 방법을 사용해야 함


def flower():
    count = 0
    startDay = [3, 1]
    endDay = [3, 1]
    checkDay = []
    for k in range(N):
        for j in range(N):
            if ((days[j][0] < startDay[0]) or (days[j][0] == startDay[0] and days[j][1] <= startDay[1])) and \
                    ((days[j][2] > endDay[0]) or (days[j][2] == endDay[0] and days[j][3] >= endDay[1])):
                checkDay = days[j]
                endDay = [days[j][2], days[j][3]]
        if [checkDay[2], checkDay[3]] == [startDay[0], startDay[1]]:
            return count
        elif checkDay:
            count += 1
        elif count == 0:
            return 0
        startDay = [checkDay[2], checkDay[3]]
        checkDay = []
    return count


print(flower())
