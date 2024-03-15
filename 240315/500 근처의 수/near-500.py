arr = list(map(int, input().split()))

max_a, min_a = 1, 1000

for a in arr:
    if a<500 and max_a<a:
        max_a = a
    if a>500 and min_a>a:
        min_a = a

print(max_a, min_a)