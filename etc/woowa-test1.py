def solution(money):
    w = 50000
    flag = 0
    array = []
    for i in range(0, 8):
        count = int(int(money) / w)
        array.append(count)
        money = int(money) - count * w
        if flag == 0:
            w = w / 5
            flag = 1
        else:
            w = w / 2
            flag = 0
    array.append(int(money))
    return array


number = input()
result = solution(number)

print("%s원은 " % format(int(number), ','), end="")
for j in range(0, 9):
    if result[j] != 0:
        if j == 0:
            print("5만 원권 %d매" % result[j], end="")
        elif j == 1:
            print("만 원권 %d매" % result[j], end="")
        elif j == 2:
            print("5천 원권 %d매" % result[j], end="")
        elif j == 3:
            print("천 원권 %d매" % result[j], end="")
        elif j == 4:
            print("500원짜리 동전 %d개" % result[j], end="")
        elif j == 5:
            print("100원짜리 동전 %d개" % result[j], end="")
        elif j == 6:
            print("50원짜리 동전 %d개" % result[j], end="")
        elif j == 7:
            print("10원짜리 동전 %d개" % result[j], end="")
        elif j == 8:
            print("1원짜리 동전 %d개" % result[j], end="")
        for k in range(j + 1, 9):
            if result[k] != 0:
                print(", ", end="")
                break
print("로 만들 수 있습니다.")
