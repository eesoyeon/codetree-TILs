A = input()
answer = ""

curr = A[0]
cnt = 1

for x in A[1:]:
    if x==curr:
        cnt += 1
    else:
        answer += curr
        answer += str(cnt)

        curr = x
        cnt = 1

answer += curr
answer += str(cnt)

print(len(answer))
print(answer)