n = int(input())
arr = list(map(int, input().split()))

answer = []
dic = {}
for a in arr:
    dic[a] = arr.count(a) 

for key in dic:
    if dic[key] == 1:
        answer.append(key)

print(max(answer) if answer else -1)