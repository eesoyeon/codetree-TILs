n = int(input())
arr = list(map(int, input().split()))

min_n = 100
for i in range(n):
    for j in range(i+1, n):
        calc = abs(arr[j] - arr[i])
        if calc < min_n:
            min_n = calc

print(min_n)