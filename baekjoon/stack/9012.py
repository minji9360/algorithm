import sys

N = int(input())
# for _ in range(N):
#     S = input()
#     result, flag, right, left = "YES", 0, 0, 0
#     for i in S:
#         if i == "(":
#             flag = 0
#         if i == ")" and flag == 0:
#             result = "NO"
#             break
#         elif i == ")" and flag == 1:
#         else:
#             right += 1
#     if left == right:
#         print("YES")
#     else:
#         print("NO")

for _ in range(N):
    S = [x for x in input()]
    S_len = len(S)
    result, index, flag, current = "YES", 0, 0, ""
    while True:
        print("======================START======================")
        print(S)
        if len(S) == 0:
            break
        elif S_len % 2 != 0 or (S_len == index and S[0] == "("):
            result = "NO"
            break
        current = S.pop()
        print(S)
        if S[-1] == ")":
            print("S[-1] == )")
            S.insert(0, current)
            flag = 0
        elif flag == 0:
            print("S[-1] == ( and flag == 0")
            S.pop()
            if S[-2] == "(":
                print("SECOND")
                flag = 1
        elif flag == 1:
            print("S[-1] == ( and flag == 1")
            flag = 0
        else:
            print("else")
            flag = 1
        index += 1
        print(S)
    print(result)
