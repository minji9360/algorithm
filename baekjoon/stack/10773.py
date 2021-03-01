N = int(input())
S = []
result = []
for _ in range(N):
    S.append(int(input()))
# for _ in range(N):
#     S.append(list(map(int, sys.stdin.readline().rsplit())))
for i in S:
    if i == 0 and len(S) != 0:
        result.pop()
    elif i != 0:
        result.append(i)
print(sum(result))
