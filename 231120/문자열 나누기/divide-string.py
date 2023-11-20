n = int(input())
string = input().split()
str_all = ""

for i in range(n):
    str_all += string[i]

leng = len(str_all)

for i in range(leng):
    print(str_all[i], end="")
    if (i+1)%5==0:
        print()