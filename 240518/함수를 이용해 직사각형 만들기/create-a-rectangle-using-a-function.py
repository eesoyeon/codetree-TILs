row, col = tuple(map(int, input().split()))

def print_rect(n, m):
    for _ in range(n):
        print("1"* m)

print_rect(row, col)