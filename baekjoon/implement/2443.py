N = int(input())

for i in range(N):
    for _ in range(i):
        print(" ", end="")
    for _ in range(i, 2*N-i-1):
        print("*", end="")
    print("")
