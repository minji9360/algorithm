N = int(input())
for i in range(N):
    for j in range(i):
        print(" ", end="")
    for k in range(N-i):
        print("*", end="")
    print("")

# for문 안에 for문을 넣어 일반적으로 짜던 코드로 짰는데, 새로운 방법을 배웠다!
# for문 하나로 N+1까지 돌린다.
# print(' '*i+'*'*(N-i)) 이 한 줄로 끝
# print 안에서 문자 * 숫자로 원하는 수만큼 문자를 출력할 수 있는걸 처음 알았다.
# 유용하게 사용할 수 있을 것 같다.