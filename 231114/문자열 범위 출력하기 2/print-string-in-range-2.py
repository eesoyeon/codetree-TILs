string = input()
n = int(input())

leng = len(string)

if n>leng:
    print(string)
else:
    for elem in string[:leng-n-1:-1]:
        print(elem, end="")