A = input()
B = input()

n = 0
# print(A[:-1])
for i in range(99):
    A = A[-1] + A[:-1]
    if A==B:
        n += 1
        break
    n += 1


if n < 99:
    print(n)
else:
    print(-1)