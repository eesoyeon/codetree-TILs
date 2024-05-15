n, t = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
cnt = 0
for i in range(n):
    if i>=1 and arr[i] - arr[i-1] == 1:
        if arr[i] > t and arr[i-1] > t:
            cnt += 1
    else:
        cnt = 1
    ans = max(ans, cnt)

if ans == 1:
    print(0)
else:
    print(ans)