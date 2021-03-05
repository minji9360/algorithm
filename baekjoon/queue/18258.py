import sys

N = int(input())
li, result = "", []


# def isEmpty(queue):
#     if len(queue) == 0:
#         return 1
#     else:
#         return 0
#

for i in range(N):
    li = sys.stdin.readline().split()

    if li[0] == "push":
        result.append(int(li[1]))
    elif li[0] == "size":
        print(len(result))
    elif li[0] == "empty":
        if len(result) == 0:
            print(1)
        else:
            print(0)
    elif len(result) == 0:
        print(-1)
    elif li[0] == "pop":
        print(result.pop(0))
    elif li[0] == "front":
        print(result[0])
    elif li[0] == "back":
        print(result[-1])
