N = int(input())
for i in range(1, N+1):
    print("*"*i+" "*(2*N-2*i)+"*"*i)
for i in range(1, N+1):
    print("*"*(N-i)+" "*(2*i)+"*"*(N-i))

# 아래 for문 실행문은 위 for문과 동일하게 하고 range를 (n, 0, -1)로 해도 됨
# 또는 for문 대신 while문을 i<n 조건 또는 1 <= i 조건을 달고, 실행문 안에 i += 1, i -= 1을 달아도 됨
