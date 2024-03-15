n = int(input())
arr = list(map(int, input().split()))

# answer = []
max_profit = 0
for i in range(n):
    for j in range(i+1, n):
        if arr[j] > arr[i]:
            profit = arr[j] - arr[i]
            # answer.append(arr[j] - arr[i])
            if profit > max_profit:
                max_profit = profit

print(max_profit)
# print(max(answer) if answer else 0)