n = int(input())

colored = [0]*200001
b, w = 0, 0
cur = 100000

for _ in range(n):
    x, direction = input().split()
    x = int(x)

    if direction=='R':
        for i in range(cur, cur+x):
            colored[i] = 1
        cur += x-1
    else:
        for i in range(cur-x+1, cur+1):
            colored[i] = 2
        cur -= x+1

for i in range(len(colored)):
    if colored[i] == 1:
        b += 1
    elif colored[i] == 2:
        w += 1

print(w, b)