a, b = tuple(map(int, input().split()))

def calculation(a, b):
    if a>b:
        b += 10
        a *= 2
    else:
        a += 10
        b *= 2
    return a, b

a, b = calculation(a, b)
print(a, b)