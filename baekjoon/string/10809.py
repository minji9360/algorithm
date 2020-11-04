import string
import sys

S = input()
if (len(S) > 100):
    print("단어의 길이는 100자까지만 가능합니다")
    sys.exit()

for i in S:
    if (not(i.islower())):
        print("소문자 영어만 입력 가능합니다.")
        sys.exit()

for i in string.ascii_lowercase:
    count = -1
    result = -1
    for j in S:
        count += 1
        if (i == j):
            result = count
            break
    print(result, end=" ")
