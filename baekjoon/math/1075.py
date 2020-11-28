N = int(input())
F = int(input())
N = int(int(N / 100) * 100)
for _ in range(99):
    if N % F == 0:
        N = str(N)
        print(N[-2:])
        break
    else:
        N += 1
