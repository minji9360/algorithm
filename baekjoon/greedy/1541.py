inputData = input()
flag = number = 0
array = []

for i in inputData:
    if "0" <= i <= "9":
        number = number * 10 + int(i)
        print(number)
        # if flag == 0:
        #     continue
        flag = 0
    else:
        flag = 1
    if flag == 1:
        array.append(number)
        array.append(i)
        number = 0
    if flag == 0 and number != "":
        array.append(number)
print(array)
