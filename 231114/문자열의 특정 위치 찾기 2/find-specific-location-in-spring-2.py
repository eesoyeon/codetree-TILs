arr = ["apple", "banana", "grape", "blueberry", "orange"]

string = input()

cnt = 0

for elem in arr:
    if elem[2]==string or elem[3]==string:
        print(elem)
        cnt += 1
print(cnt)