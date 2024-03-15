n1, n2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def is_sequence(A, B):
    cnt = 0
    for i in range(n1-n2+1):
        if A[i:i+n2] == B:
            cnt += 1
    if cnt!=0:
        return True
    else:
        return False
        
if is_sequence(A, B):
    print("Yes")
else:
    print("No")