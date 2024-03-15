A = input()
B = input()

leng = len(A)
n = 0
# print(A[:-1])
for i in range(leng):
    A = A[-1] + A[:-1]
    n += 1

    if A==B:
        print(n)
        break
    
    if i == leng-1: print(-1)