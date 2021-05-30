vowels = ['a', 'e', 'i', 'o', 'u']

while True:
  N = 0
  S = input()
  if S == "#":
    break
  S = S.lower()
  for x in vowels:
    N += S.count(x)
  print(N)
