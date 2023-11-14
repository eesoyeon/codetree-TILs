arr = [
    input()
    for _ in range(10)
]

c = input()

for elem in arr:
    if elem[-1] == c:
        print(elem)
    else:
        print('None')