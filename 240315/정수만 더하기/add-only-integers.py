A = input()

answer = 0
for a in A:
    if a.isdigit():
        answer += int(a)

print(answer)