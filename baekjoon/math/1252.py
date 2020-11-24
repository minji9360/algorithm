a, b = input().split()
a = int(a, 2)
b = int(b, 2)
c = bin(a + b)
for i in c[2:]:
    print(i, end="")
