li = list(input())

stack_li = []

for i in li:
    if i=='(':
        stack_li.append(i)
    else:
        if stack_li!=[]:
            stack_li.pop()

if stack_li==[]:
    print("Yes")
else:
    print('No')