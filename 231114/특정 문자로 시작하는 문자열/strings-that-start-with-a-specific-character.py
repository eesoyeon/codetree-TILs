n = int(input())
arr = [
    input()
    for _ in range(n)
]
c = input()

cnt = 0
leng = 0
for elem in arr:
    if elem[0]==c:
        cnt += 1
        leng += len(elem)

print(cnt, "{:.2f}".format(leng/cnt))