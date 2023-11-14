n = int(input())
arr = [
    input()
    for _ in range(n)
]

cnt = 0
f = 0
for elem in arr:
    cnt += len(elem)
    if elem[0]=='a':
        f += 1
    
print(cnt, f)