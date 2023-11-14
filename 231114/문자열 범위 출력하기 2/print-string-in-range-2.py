string = input()
n = int(input())

leng = len(string)

for elem in string[:leng-n-1:-1]:
    print(elem, end="")

if n>leng:
    print(string)