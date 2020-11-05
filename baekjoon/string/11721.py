import sys

N = input()
if (len(N) == 0) or (len(N) > 100):
    print("단어의 길이는 0 이상 100 이하여야 합니다.")
    sys.exit()
elif not(N.isalpha()):
    print("단어는 알파벳 소문자와 대문자로만 이루어져야 합니다.")
    sys.exit()

for i in range(0, len(N)):
    if (i != 0) & (i % 10 == 0):
        print("")
    print(N[i], end="")
