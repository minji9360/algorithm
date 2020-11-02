A = int(input())
B = int(input())
C = int(input())
calc = str(A * B * C)

for i in range(0, 10):
    result = 0
    for j in calc:
        if int(i) == int(j):
            result += 1
    print("%d" % result)