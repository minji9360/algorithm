N, M = map(int, input().split())
array = []
result = 0

for _ in range(N):
    a = list(map(int, input().split()))
    array.append(a)
for i in range(N):
    minNum = 99999
    for j in range(M):
        if array[i][j] < minNum:
            minNum = array[i][j]
    if result < minNum:
        result = minNum
print(result)
