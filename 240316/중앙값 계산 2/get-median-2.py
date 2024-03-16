n = int(input())
li = list(map(int, input().split()))

ans = []
for i in range(n):
    x = []
    if li[i]%2!=0:
        x = sorted(li[:i+1])
        ans.append(x[i//2])
        # ans.append(li[])
        # x.append(li[:i+1])

for elem in ans:
    print(elem, end=" ")