n = int(input())

for i in range(n):
    for j in range(n):
        #j 짝수일때 
        if j%2==0:
            if i==0:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        else:
            if i<=j:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()