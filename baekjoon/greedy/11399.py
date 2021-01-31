N = int(input())
time = list(map(int, input().split()))

time.sort()
now_time = 0
total_time = 0
for i in time:
    now_time += i
    total_time += now_time
print(total_time)
