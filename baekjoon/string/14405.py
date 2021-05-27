S = input()

S = S.replace("pi", "")
S = S.replace("ka", "")
S = S.replace("chu", "")

if len(S) == 0:
    print("YES")
else:
    print("NO")
