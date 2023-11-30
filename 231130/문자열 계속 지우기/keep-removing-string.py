a = input()
b = input()

leng = len(b)
index = a.find(b)
while index>-1:
    index = a.find(b)
    a = a[:index] + a[index+leng:]

print(a)


# for i in range(len(a)):
#     a = [:index] + [index+leng:]
#     print(a)