n = int(input())

tile = [
    tuple(input().split())
    for _ in range(n)
]

colored = [0] * 200001
cur_dir = 10000

# L: 흰색, R: 검은색 / 흰색2, 검은색2번 이상이면 회색
white, black = [0] * 200001, [0] * 200001
w, b, g = 0, 0, 0

for x, location in tile:
    x = int(x)

    if location == 'L':
        for i in range(cur_dir-x, cur_dir):
            colored[i] += 1
            white[i] += 1
        cur_dir -= x
    else:
        for i in range(cur_dir, cur_dir+x):
            colored[i] += 1
            black[i] += 1
        cur_dir += x

for i in range(len(colored)):
    if colored[i] > 0:
        if white[i] >=2 and black[i] >=2:
            g += 1
        elif colored[i]%2==1:
            w += 1
        else:
            b += 1
    

print(w, b, g, end=" ")