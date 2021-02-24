S = input()
numOne = S.split("0")
numZero = S.split("1")
cntOne = len(numOne) - numOne.count("")
cntZero = len(numZero) - numZero.count("")

print(min(cntOne, cntZero))
