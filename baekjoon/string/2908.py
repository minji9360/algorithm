import sys
A, B = input().split(" ")

if (A == 0) or (B == 0) or (A == B) or (int(A) < 100) or (int(B) < 100) or (int(A) > 999) or (int(B) > 999):
    print("두 수의 조건이 맞는지 확인해주세요.")
    sys.exit()

number1 = number2 = 0
count = 1

for i in range(0, 3):
    number1 += int(A[i]) * count
    number2 += int(B[i]) * count
    count *= 10

if number1 > number2:
    print(number1)
elif number1 < number2:
    print(number2)
