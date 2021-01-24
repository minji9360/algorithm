price = int(input())
A, B, C, D = 0, 0, 0, 0
if price / 500 > 0:
    A = int(price / 500)
    price %= 500
if price / 100 > 0:
    B = int(price / 100)
    price %= 100
if price / 50 > 0:
    C = int(price / 50)
    price %= 50
if price / 10 > 0:
    D = int(price / 10)
    price %= 10
print(A + B + C + D)
