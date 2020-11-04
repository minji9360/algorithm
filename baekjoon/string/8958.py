import sys

N = int(input())
for i in range(0, N):
    S = input()
    if (len(S) >= 80):
        print("길이는 80 미만이어야 합니다.")
        sys.exit()
    score = 0
    result = 0

    for i in S:
        if (i == "O"):
            score += 1
            result += score
        elif (i == "X"):
            score = 0
        else:
            print("O나 X만 입력할 수 있습니다.")
            sys.exit()
    print(result)
