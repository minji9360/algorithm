a = []
min_burger = 2100
min_drink = 2100
for i in range(5):
    a.append(int(input()))
for i in a[:3]:
    if i < min_burger:
        min_burger = i
for i in a[3:5]:
    if i < min_drink:
        min_drink = i
print(min_burger + min_drink - 50)
