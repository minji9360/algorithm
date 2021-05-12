N = int(input())
deque = list(range(1, N + 1))
del_num = 0

while 1:
  del_num = deque[0]
  deque.remove(del_num)
  print(del_num, end=" ")

  if len(deque) == 1:
    print(deque[0])
    break
  else:
    next_num = deque[0]
    deque.remove(next_num)
    deque.append(next_num)
