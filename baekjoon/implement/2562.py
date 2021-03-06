max_num = max_index = 0

for i in range(9):
    S = int(input())
    if S > max_num:
        max_num = S
        max_index = i + 1
print(max_num, max_index, end="\n")
