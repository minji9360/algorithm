N, K = map(int, input().split())
seq = input().split()
using = []
index = [-1 for _ in range(N)]
flag = count = 0

for i in range(N):
    using.append(int(seq[i]))
for i in range(N, K):
    for j in range(N):
        if int(seq[i]) == using[j]:
            continue
        else:
            for k in range(i, K):
                if int(seq[k]) == using[j] and index[j] == -1:
                    index[j] = k
                    break
            # if index.index(-1):
            #     print("반복 X")
            # if int(seq[i]) == using[j] and index[j] == -1:
            #     index[j] = i
            #     break
print(seq)
print(using)
print(index)
