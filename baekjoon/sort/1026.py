N = int(input())
A = B = []
result = 0
# A = input().split()
# B = input().split()
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

A.sort()
B.sort(reverse=True)
for i in range(N):
    result += A[i] * B[i]
print(result)