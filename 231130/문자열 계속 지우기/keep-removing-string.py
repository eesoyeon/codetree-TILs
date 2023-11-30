a = input()
b = input()

leng = len(b)

while a.find(b)>-1:
    index = a.find(b)
    a = a[:index] + a[index+leng:]

print(a)


# for i in range(len(a)):
#     a = [:index] + [index+leng:]
#     print(a)