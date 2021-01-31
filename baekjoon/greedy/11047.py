N, K = map(int, input().split())
coin_kind = []
total_coin = 0

for _ in range(N):
    coin_kind.append(int(input()))
coin_kind.sort(reverse=True)
for i in coin_kind:
    if i <= K:
        coin = K // i
        K -= (K // i) * i
        total_coin += coin
print(total_coin)
