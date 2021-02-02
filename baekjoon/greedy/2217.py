import sys

N = int(sys.stdin.readline())
rope = list()
max_kg = 0

for _ in range(N):
    rope.append(int(sys.stdin.readline().strip()))
rope.sort()
for i in range(N):
    max_kg = max(max_kg, int(rope[i]) * (N - i))
print(max_kg)
