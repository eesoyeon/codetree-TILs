a = list(input())
b = list(input())

a.sort()
b.sort()

if a == b and len(a) == len(b):
    print("Yes")
else:
    print("No")