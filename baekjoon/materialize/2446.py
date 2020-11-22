N = int(input())
for i in range(N):
    print(" "*i+"*"*(2*N-2*i-1))
for i in range(N-1, 0, -1):
    print(" "*(i-1)+"*"*(2*N-2*i+1))

# 헐 여기 abs 함수 쓰면 되네.. abs 써서 해보기
