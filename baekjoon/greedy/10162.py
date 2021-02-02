import sys

T = int(sys.stdin.readline())
A, B, C = 300, 60, 10
A_count, B_count, C_count = 0, 0, 0

if T // A > 0:
    A_count = T // A
    T %= A
if T // B > 0:
    B_count = T // B
    T %= B
if T // C > 0:
    C_count = T // C
    T %= C
if T == 0:
    print(A_count, B_count, C_count)
else:
    print(-1)
