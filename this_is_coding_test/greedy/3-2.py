N, M, K = map(int, input().split(" "))
array = list(map(int, input().split(" ")))
sumNum = 0

array.sort(reverse=True)
for i in range(0, M):
    if i == 0 or i % K != 0:
        sumNum += array[0]
    else:
        sumNum += array[1]
print(sumNum)
