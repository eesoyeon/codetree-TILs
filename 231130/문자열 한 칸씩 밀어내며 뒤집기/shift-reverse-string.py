s, q = input().split()
q = int(q)

for _ in range(q):
    n = int(input())
    if n==1:
        s = s[1:len(s)] + s[0]
    elif n==2:
        s = s[-1] + s[:-1]
    else:
        s = s[::-1]
    print(s)