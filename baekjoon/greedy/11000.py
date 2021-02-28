N = int(input())
T = [[0, 0] for _ in range(N)]
current = [[0, 0] for _ in range(N)]
count = 0
end = 0
for i in range(N):
    T[i][0], T[i][1] = map(int, input().split())
print(T)
for i in range(N):
    start = current[i][0]
    end = start
    print(T[i][0])
    if T[i][0] < end:
        continue
    for j in range(N):
        if end < T[j][1]:
            # 현재 시작 시각 < 이전 종료 시각 and 저장된 종료 시각 < 현재 종료 시각
            continue
        start = T[j][0]
        end = T[j][1]
    print(start)
    print(end)
    current[i] = [start, end]
    print(current)
    count += 1
print(count)
