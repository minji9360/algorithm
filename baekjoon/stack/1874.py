n = int(input())
stack = []  # 기존 입력받는 데이터
sort = []  # 1부터 n까지 오름차순 정렬됨
comp = []  # 새로 넣으며 비교
result = []  # +, - 저장
flag = 0

# stack, sort 입력
for i in range(n):
    stack.append(int(input()))
    sort.append(i + 1)
# sort.append(-1)
print(stack)

# while True:
#     if len(stack) == 0:
#         break
#     # print("================================================ " + str(i))
#     comp.append(sort[0])
#     result.append("+")
#     if stack[-1] == comp[-1]:
#         sort.pop(0)
#         stack.pop()
#     else:
#         sort.append(comp[-1])
#         sort.pop(0)
#         comp.pop()
#         result.append("-")
#         print("NONONONONONONONO")
    # else:

# while True:
# # for _ in range(10):
#     if len(stack) == 0:
#         break
#     print("================================================ ")
#     comp.append(sort[0])
#     sort.pop(0)
#     result.append("+")
#     if stack[-1] != comp[-1]:
#         flag += 1
#         sort.append(comp[-1])
#         comp.pop()
#     elif flag > 1:
#         result.pop()
#         for _ in range(flag):
#             result.append("-")
#         flag = 0
#         stack.pop()
#     elif flag == 1:
#         for _ in range(flag):
#             result.append("-")
#         flag = 0
#         stack.pop()
#     elif flag == 0:
#         stack.pop()
#     print("----stack----")
#     print(stack)
#     print("----comp----")
#     print(comp)
#     print("----sort----")
#     print(sort)
#     print("----result----")
#     print(result)

while True:
# for _ in range(10):
    if len(stack) == 0:
        break
    print("================================================ ")
    # if sort[0] == -1:
    #     break
    if sort[0] == stack[-1]:
        if flag != 0:
            for _ in range(flag):
                result.append("-")
            flag = 0
        comp.append(sort[0])
        stack.pop()
        sort.pop(0)
    else:
        sort.append(sort[0])
        sort.pop(0)
        flag += 1
    result.append("+")
for _ in range(len(comp)):
    result.append("-")
    # print("----stack----")
    # print(stack)
    print("----comp----")
    print(comp)
    # print("----sort----")
    # print(sort)
    # print("----result----")
print(result)
