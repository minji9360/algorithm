T = int(input())
for i in range(1, T+1):
    A, B = input().split(' ')
    print("Case #%d: %s + %s = %d" % (i, A, B, int(A) + int(B)))
