import sys

alpha = input()
time = 0

if len(alpha) < 2 or len(alpha) > 15:
    print("단어는 2글자 이상 15글자 이하로 입력해주세요.")
    sys.exit()
elif not alpha.isupper():
    print("단어는 영어 대문자만 입력 가능합니다.")
    sys.exit()


def is_which_number(s):
    if s == "A" or s == "B" or s == "C":
        return 2
    elif s == "D" or s == "E" or s == "F":
        return 3
    elif s == "G" or s == "H" or s == "I":
        return 4
    elif s == "J" or s == "K" or s == "L":
        return 5
    elif s == "M" or s == "N" or s == "O":
        return 6
    elif s == "P" or s == "Q" or s == "R" or s == "S":
        return 7
    elif s == "T" or s == "U" or s == "V":
        return 8
    else:
        return 9


for i in alpha:
    time += is_which_number(i) + 1
print(time)
