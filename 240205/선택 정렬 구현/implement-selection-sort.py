n = int(input())
arr = list(map(int, input().split()))

def selection_sort(arr):
    for i in range(n-1):
        min_val = i
        for j in range(i+1, n):
            if arr[j] < arr[min_val]:
                min_val = j
        tmp = arr[i]
        arr[i] = arr[min_val]
        arr[min_val] = tmp

selection_sort(arr)

for elem in arr:
    print(elem, end=" ")