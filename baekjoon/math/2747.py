n = int(input())
temp = 0
front = 0
back = 1
result = 0
for i in range(0, n - 1):
    temp = front
    front = back
    back += temp
print(back)

# 처음에는 front에 back을 더하기만 해서 총 합을 출력해서 틀림
# 다시 생각해서 피보나치 수를 계산하는대로 다시 풀어서 통과
