arr = [
    input()
    for _ in range(10)
]

c = input()

cnt = 0
for elem in arr:
    if elem[-1] == c:
        print(elem)
        cnt += 1


if cnt==0:
    print("None")