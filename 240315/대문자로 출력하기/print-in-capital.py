s = input()

new_s = ""

for char in s:
    if char.isalpha():
        new_s += char

print(new_s.upper())