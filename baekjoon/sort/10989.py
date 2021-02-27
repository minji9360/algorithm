N = int(input())
arr = [0 for _ in range(N)]
for i in range(N):
    arr[i] = int(input())
arr.sort()
for i in range(N):
    print(arr[i])
