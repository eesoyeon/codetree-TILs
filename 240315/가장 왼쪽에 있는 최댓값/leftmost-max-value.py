n = int(input())
arr = list(map(int, input().split()))

answer = []

i = 0
while i!= 1:
    i = arr.index(max(arr)) + 1
    answer.append(i)
    arr = arr[:i-1]
    
for a in answer:
    print(a, end=" ")