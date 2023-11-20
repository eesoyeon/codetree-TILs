string = input()

if len(string)%2==0:
    for elem in string[::-2]:
        print(elem, end="")
else:
    for elem in string[len(string)-1::-2]:
        print(elem, end="")