A = input()

answer = 0
for a in A:
    if ord(a) >= ord('0') and ord(a) <= ord('9'):
        answer += ord(a) - ord('0')

print(answer)