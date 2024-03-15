n = int(input())
arr = list(map(int, input().split()))

benefit = 0
max_b = 0
for i in range(n):
    for j in range(i, n):
        if arr[j] > arr[i]:
            benefit = arr[j] - arr[i]
    if benefit>max_b:
        max_b = benefit

print(max_b if max_b!= 0 else 0)