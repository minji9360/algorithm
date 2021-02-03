import sys

N = int(sys.stdin.readline())
movement = list(sys.stdin.readline().strip().split())
current_x = current_y = 1

for direction in movement:
    if direction == "R":
        if current_y == N:
            continue
        current_y += 1
    elif direction == "L":
        if current_y == 1:
            continue
        current_y -= 1
    elif direction == "U":
        if current_x == 1:
            continue
        current_x -= 1
    elif direction == "D":
        if current_x == N:
            continue
        current_x += 1
print(current_x, current_y)
