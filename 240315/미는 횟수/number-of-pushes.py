A = input()
B = input()

n = 0
# print(A[:-1])
for i in range(100):
    A = A[-1] + A[:-1]
    if A == B:
        n = i+1
        break

if n<100:
    print(n)
else:
    print(-1)