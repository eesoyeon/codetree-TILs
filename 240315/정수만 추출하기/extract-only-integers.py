a, b = input().split()

new_a, new_b = "", ""

for x in a:
    if ord(x)>=ord('0') and ord(x)<=ord('9'):
        new_a += x
    else:
        break

for y in b:
    if ord(y)>=ord('0') and ord(y)<=ord('9'):
        new_b += y
    else:
        break

print(int(new_a)+int(new_b))