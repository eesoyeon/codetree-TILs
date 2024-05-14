n = int(input())

li = [[0]*201 for _ in range(201)]
OFFSET = 100

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1 += OFFSET
    y1 += OFFSET
    x2 += OFFSET
    y2 += OFFSET


    for x in range(x1, x2):
        for y in range(y1, y2):
            li[x][y] = 1

answer = 0
for x in range(201):
    for y in range(201):
        if li[x][y]:
            answer += 1

print(answer)