n = int(input())
li = [int(input()) for _ in range(n)]

answer = 0
cnt = 0
for i in range(n):
    if i>=1 and li[i] == li[i-1]:
        cnt += 1
    else:
        cnt = 1
    
    answer = max(answer, cnt)

print(answer)