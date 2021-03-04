import sys

N = int(input())
li = []
result = []


def isEmpty(queue):
    if len(queue) == 0:
        return 1
    else:
        return 0


for i in range(N):
    li.append(sys.stdin.readline().split())
for i in range(N):
    if li[i][0] == "push":
        result.append(int(li[i][1]))
        print(result[-1])
    elif li[i][0] == "pop":
        print(result.pop())
    elif li[i][0] == "size":
        print(len(result))
    elif li[i][0] == "front":
        print(result[0])
    elif li[i][0] == "back":
        print(result[-1])
    elif li[i][0] == "empty":
        print(isEmpty(result))