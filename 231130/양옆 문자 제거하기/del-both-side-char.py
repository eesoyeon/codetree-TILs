s = input()
leng = len(s)

#5-2 = 3
result = s[:2] + s[3:leng-2] + s[leng-1:]
print(result)