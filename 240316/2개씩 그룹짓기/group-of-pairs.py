n = int(input())
li = list(map(int, input().split()))
li.sort()

group_max =0

for i in range(n):
    group_sum = li[i] + li[2*n-1-i]
    if group_sum > group_max:
        group_max = group_sum
print(group_max)