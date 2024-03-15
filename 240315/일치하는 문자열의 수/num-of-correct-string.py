n, A = input().split()
n = int(n)

li = [input() for i in range(n)]
ans = 0 

for l in li:
    if l==A:
        ans += 1

print(ans)