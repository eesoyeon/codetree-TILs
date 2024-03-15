a = input()
cmd = list(input())

for i in range(len(cmd)):
    if cmd[i] == 'L':
        a = a[1:] + a[0]
    elif cmd[i] == 'R':
        a = a[-1] + a[:-1]

print(a)