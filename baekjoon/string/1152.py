import sys

S = input()
if len(S) > 1000000:
    print("문자열의 길이는 1,000,000 이하여야 합니다.")
    sys.exit()

flag = -1
count = 0
for i in S:
    if (flag == -1 or flag == 0) & i.isalpha():
        flag = 1
        count += 1
    elif i == " ":
        flag = 0
    elif not(i.isalpha() or i == " "):
        print("공백 문자나 영어 대소문자만 입력할 수 있습니다.")
        sys.exit()
print(count)
