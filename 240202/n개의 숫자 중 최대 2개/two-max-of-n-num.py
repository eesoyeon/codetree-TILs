n = int(input())
arr = list(map(int, input().split()))

max_val = arr[0]
max2_val = arr[0]

for elem in arr[1:]:
    if elem>max_val:
        max_val=elem

arr.remove(max_val)
for elem in arr[1:]:
    if elem>max2_val:
        max2_val=elem
    
print(max_val, max2_val)