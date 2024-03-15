s = input()

for char in s:
    if ord(char) >= ord('A') and ord(char) <= ord('Z'):
        print(char.lower(), end="")
    else:
        print(char.upper(), end="")