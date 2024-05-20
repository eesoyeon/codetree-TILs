n = int(input())
li = list(map(int, input().split()))

def recur(n, li):
    if n==1:
        return li[0]

    lastone = recur(n-1, li)
    for i in range(li[n-1], 0, -1):
        if li[n-1] % i == 0 and lastone % i == 0:
            return lastone // i * li[n-1]


print(recur(n, li))