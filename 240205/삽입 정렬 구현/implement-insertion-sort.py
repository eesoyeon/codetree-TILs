n = int(input())
arr = list(map(int, input().split()))

def insertionSort():
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

insertionSort()

for elem in arr:
    print(elem, end=" ")