a = input()
b = input()

new_a, new_b = "", ""

for x in a:
    if x.isdigit():
        new_a += x

for x in b:
    if x.isdigit():
        new_b += x

print(int(new_a)+int(new_b))