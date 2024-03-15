a, b = map(int, input().split())

val = str(a+b)
answer = 0

for v in val:
    if v=='1':
        answer += 1

print(answer)