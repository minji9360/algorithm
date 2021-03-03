import sys

try:
    while True:
        N = int(input())
        S = []
        for _ in range(N):
            S.append(int(sys.stdin.readline().rstrip()))
        sumVal = sum(S)
        if sumVal == 0:
            print(0)
        elif sumVal > 0:
            print("+")
        else:
            print("-")
except:
    exit()
