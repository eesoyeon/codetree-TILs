s, q = input().split()
s = list(s)
q = int(q)


for _ in range(q):
    arr = list(input().split())
    arr[0] = int(arr[0])
    if arr[0] == 1:
        a, b = int(arr[1]), int(arr[2])
        s[a-1], s[b-1] = s[b-1], s[a-1]
        print(''.join(s))
    elif arr[0] == 2:
        s = ''.join(s)
        s = s.replace(arr[1], arr[2])
        print(s)