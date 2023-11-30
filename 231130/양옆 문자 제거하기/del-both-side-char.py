s = input()
leng = len(s)

#5-2 = 3
result = s[:1] + s[2:leng-2] + s[leng-1:]
print(result)