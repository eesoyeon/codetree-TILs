commands = input()

cur_dir = 3
x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

for command in commands:
    if command == 'L':
        cur_dir = (cur_dir-1 + 4) % 4
    elif command == 'R':
        cur_dir = (cur_dir + 1) % 4
    else:
        x, y = x + dx[cur_dir], y + dy[cur_dir]

print(x, y)