import string
import sys

S = input().upper()

if len(S) > 1000000:
    print("입력값의 길이는 1,000,000자 이하여야 합니다.")
    sys.exit()

count1 = count2 = 0
alpha1 = alpha2 = ""

for i in string.ascii_uppercase:
    temp_count = 0
    for j in S:
        if j == i:
            temp_count += 1
    if count1 < temp_count:
        count1 = temp_count
        alpha1 = i
    elif count2 < temp_count:
        count2 = temp_count
        alpha2 = i
if count1 == count2:
    print("?")
else:
    print(alpha1)
