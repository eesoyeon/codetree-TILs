li = list(input())

stack_li = []

answer = 'Yes'
for i in li:
    if i=='(':
        stack_li.append(i)
    else:
        if stack_li==[]:
            answer = 'No'
            break
        else:
            stack_li.pop()

if stack_li!=[]:
    answer = 'No'

print(answer)