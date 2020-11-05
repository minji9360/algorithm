import sys
T = int(input())

if (T < 1) or (T > 1000):
    print("테스트 케이스의 개수는 1 이상 1000 이하여야 합니다.")
    sys.exit()

for i in range(0, T):
    R, S = input().split(" ")

    if (len(R) < 1) or (len(R) > 8):
        print("반복 횟수는 1 이상 8 이하여야 합니다.")
        sys.exit()
    elif (len(S) < 1) or (len(S) > 20):
        print("문자열의 길이는 1 이상 20 이하여야 합니다.")
        sys.exit()

    for j in S:
        for k in range(0, int(R)):
            print(j, end="")
    print("")
