li = [tuple(map(int, input().split())) for _ in range(2)]
m = [tuple(map(int, input().split()))]
sq = [[0]*2001 for _ in range(2001)]

OFFSET = 1000

for x1, y1, x2, y2 in li:
    x1 += OFFSET
    y1 += OFFSET
    x2 += OFFSET
    y2 += OFFSET

    for row in range(x1, x2):
        for col in range(y1, y2):
            sq[row][col] += 1

for x1, y1, x2, y2 in m:
    x1 += OFFSET
    y1 += OFFSET
    x2 += OFFSET
    y2 += OFFSET

    for row in range(x1, x2):
        for col in range(y1, y2):
            sq[row][col] += 2


area = 0
for x in range(2001):
    for y in range(2001):
        if sq[x][y]==1:
            area += 1
print(area)