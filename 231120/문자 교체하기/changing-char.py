a, b = input().split()

c = list(a)
d = list(b)

new = c[:2] + d[2:]
print("".join(new))