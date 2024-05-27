li = list(input())

stack_li = []

for i in li:
    if i=='(':
        stack_li.append(i)
    else:
        stack_li.pop()

if len(stack_li)==0:
    print("Yes")
else:
    print("No")