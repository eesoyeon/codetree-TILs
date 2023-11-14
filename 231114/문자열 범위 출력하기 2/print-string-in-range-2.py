string = input()
n = int(input())

leng = len(string)

if n>leng:
    for elem in string[::-1]:
        print(elem, end="")
else:
    for elem in string[:n-leng-1:-1]:
        print(elem, end="")