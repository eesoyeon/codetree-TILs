n = int(input())

d = ['W', 'S', 'N', 'E']
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

x, y = 0, 0
for _ in range(n):
    a, b = input().split()
    b = int(b)

    x += dx[d.index(a)]*b
    y += dy[d.index(a)]*b
    
print(x, y)