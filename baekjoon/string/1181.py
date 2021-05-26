import sys

N = int(sys.stdin.readline())
words = [sys.stdin.readline().strip() for i in range(N)]

words = list(set(words))
words.sort()
words.sort(key=len)

for i in words:
    print(i)
