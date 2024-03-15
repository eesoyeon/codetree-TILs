A = input()
B = input()

n = 0
# print(A[:-1])
for i in range(100):
    A = A[-1] + A[:-1]
    if A == B:
        print(i+1)
        break
    else: continue
    print(-1)