inputVal = input()
grade = []
result = 0

grades = {"A":4, "B":3, "C":2, "D":1, "F":0}
steps = {"+": 0.3, "0":0.0, "-":-0.3}

if len(inputVal) == 1:
  result += grades[inputVal]
else:
  result += grades[inputVal[0]]
  result += steps[inputVal[1]]

print(float(result))
