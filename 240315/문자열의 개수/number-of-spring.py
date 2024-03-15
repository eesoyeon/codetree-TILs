cnt = 0
ans = []

for i in range(1, 201):
    a = input()
    if a=='0':
        break
    cnt += 1

    if i%2!=0:
        ans.append(a)

print(cnt)
for x in ans:
    print(x)