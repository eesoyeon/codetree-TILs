n = int(input())
stack_li = []

for _ in range(n):
    command = list(input().split())

    if command[0] == 'push':
        stack_li.append(command[1])
    elif command[0] == 'pop':
        print(stack_li[-1])
        stack_li.pop()
    elif command[0] == 'size':
        print(len(stack_li))
    elif command[0] == 'empty':
        print(1) if len(stack_li) == 0 else print(0)
    else:
        print(stack_li[-1])