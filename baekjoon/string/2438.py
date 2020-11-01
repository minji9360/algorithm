N = input("N은?")
N = int(N)
i = 1
if (N >= 1 & N <= 100):
    for i in range(1, N+1):
        for j in range(i):
            print("*", end="")
        print()
else:
    print("입력값이 잘못되었습니다.")