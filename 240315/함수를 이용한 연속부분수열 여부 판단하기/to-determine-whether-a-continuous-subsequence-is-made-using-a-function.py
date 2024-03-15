n1, n2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def is_sequence(A, B):
    for i in range(n1-n2+1):
        if A[i:i+n2] == B:
            return True
        else:
            return False

if is_sequence:
    print("Yes")
else:
    print("No")