S = input()
numOne = S.split("0")
numZero = S.split("1")
cntOne = len(numOne) - numOne.count("")
cntZero = len(numZero) - numZero.count("")

if cntOne > cntZero:
    print(cntZero)
else:
    print(cntOne)
