n = int(input())
arr = list(map(int, input().split()))

min_n = arr[1] - arr[0]
for i in range(2, n):
    if min_n > arr[i] - arr[i-1]:
        min_n = arr[i] - arr[i-1]

print(min_n)