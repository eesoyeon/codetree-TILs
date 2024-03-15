n = int(input())
arr = list(map(int, input().split()))

answer = []

for i in range(n):
    max_b = 1
    for j in range(i, n):
        if arr[j] > arr[i]:
            answer.append(arr[j] - arr[i])

print(max(answer) if answer else 0)