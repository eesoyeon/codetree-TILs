a = list(input())
b = list(input())

a.sort()
b.sort()

if len(a) != len(b):
    print("No")
elif a == b:
    print("Yes")