inputData = input()
number = result = flag = 0
array = []

for i in range(len(inputData)):
    if "0" <= inputData[i] <= "9":
        number = number * 10 + int(inputData[i])
    else:
        array.append(number)
        array.append(inputData[i])
        number = 0
    if i == len(inputData) - 1:
        array.append(number)

for i in range(len(array)):
    if array[i] == "-":
        flag = 1
        continue
    if flag == 0 and type(array[i]) == int:
        result += int(array[i])
    elif flag == 1 and type(array[i]) == int:
        result -= int(array[i])

print(result)
