color = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
value = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
multiple = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]
first = input()
second = input()
third = input()
for i in range(10):
    if color[i] == first:
        first = value[i]
    if color[i] == second:
        second = value[i]
    if color[i] == third:
        third = multiple[i]
print((first * 10 + second) * third)

# if문에서 color[i] is first:로 안먹힘. 그 바로 아래줄 first is value[i]도 안먹힘
# is를 언제 쓰고 언제 안쓰는지 잘 알아야 할 듯