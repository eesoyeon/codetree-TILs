s = input()
leng = len(s)

while leng>1:
    n = int(input())
    leng -= 1
    if n>leng:
        s = s[:leng]
    else:
        s = s[:n] + s[n+1:]
    print(s)