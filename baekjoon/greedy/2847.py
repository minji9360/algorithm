N = int(input())
array = []
count = 0
for i in range(N):
    array.append(int(input()))

for i in range(N - 1, 0, -1):
    if i == 0:
        break
    if array[i] == array[i - 1]:
        count += 1
        array[i - 1] -= 1
    elif array[i] < array[i - 1]:
        count += array[i - 1] - array[i] + 1
        array[i - 1] -= array[i - 1] - array[i] + 1
print(count)
