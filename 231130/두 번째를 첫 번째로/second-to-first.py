s = input()

second = s[1]

for i in range(len(s)):
    if s[i] == second:
        s = s.replace(s[i], s[0])

print(s)