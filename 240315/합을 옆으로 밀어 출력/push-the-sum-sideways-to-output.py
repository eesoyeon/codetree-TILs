n = int(input())

arr = [int(input()) for i in range(n)]

val = str(sum(arr))

print(val[1:] + val[0])