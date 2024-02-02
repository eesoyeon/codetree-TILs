n = int(input())
arr = list(map(int, input().split()))

new_arr = []

for i in range(n):
    for j in range(i+1, n):
        if arr[i] != arr[j]:
            new_arr.append(arr[i])

if len(new_arr)==0:
    print(-1)
else:
    print(max(new_arr))