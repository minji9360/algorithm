N = int(input())
temp = zero = result = 0
minus = []
plus = []
for _ in range(N):
    temp = int(input())
    if temp < 0:
        minus.append(temp)
    elif temp > 0:
        plus.append(temp)
    else:
        zero = 1
minus.sort()
plus.sort(reverse=True)

for i in range(0, len(minus), 2):
    if i == len(minus) - 1:
        if len(minus) % 2 == 1 and zero == 0:
            result += minus[i]
        break
    result += minus[i] * minus[i + 1]
for i in range(0, len(plus), 2):
    if i == len(plus) - 1:
        if len(plus) % 2 == 1:
            result += plus[i]
        break
    result += plus[i] * plus[i + 1]
print(result)
