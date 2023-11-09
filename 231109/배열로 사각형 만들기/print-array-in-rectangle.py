n = 5
arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for j in range(5):
    arr[0][j] = 1
    arr[j][0] = 1

for i in range(1, n):
    for j in range(1, n):
        arr[i][j] = arr[i][j-1] + arr[i-1][j] 

for row in arr:
    for elem in row:
        print(elem, end=" ")
    print()