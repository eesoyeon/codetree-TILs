n = int(input())

li = [[0]*201 for i in range(201)]
OFFSET = 100

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1 += OFFSET
    y1 += OFFSET
    x2 += OFFSET
    y2 += OFFSET

    for row in range(x1, x2):
        for col in range(y1, y2):
            li[row][col] = 1

ans = 0
for row in range(201):
    for col in range(201):
        if li[row][col] == 1:
            ans += 1

print(ans)