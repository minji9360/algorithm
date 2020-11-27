while 1:
    a = input()
    chk = 0
    if int(a) == 0:
        break
    for i in range(0, int(len(a) / 2)):
        if int(a[i]) is not int(a[-(1+i)]):
            chk = -1
    if chk == -1:
        print("no")
    else:
        print("yes")
