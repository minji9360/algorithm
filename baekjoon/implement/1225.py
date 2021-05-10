num1, num2 = input().split()
num1, num2 = list(num1), list(num2)
result = 0

for a in num1:
    for b in num2:
        result += int(a) * int(b)

print(result)
