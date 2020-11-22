N = int(input())
for i in range(1, N+1):
    print(" "*(N-i), end="")
    for j in range(i):
        print("* ", end="")
    print("")

# 코드를 짜긴 했는데 그냥 고치다보니 된거.. 정확히 이게 이래서 이렇게 되겠다! 는 아니었음..
# 마지막 공백 안생기게 하려고 머리 싸맸는데 상관 없는거였다.
# 공백 상관 없으면 print(" "*(n-i)+"* *i)로 해결 가능
