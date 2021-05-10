from itertools import product

num1, num2 = input().split()
num = [list(map(int, num1)), list(map(int, num2))]

num = list(product(*num))
result = 0

for x in num:
    result += x[0] * x[1]
print(result)
