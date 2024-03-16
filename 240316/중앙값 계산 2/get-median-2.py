n = int(input())
li = list(map(int, input().split()))

ans = []
for i in range(0, n+1, 2):
    x = sorted(li[:i+1])
    ans.append(x[i//2])
    # ans.append(li[])
    # x.append(li[:i+1])

for elem in ans:
    print(elem, end=" ")