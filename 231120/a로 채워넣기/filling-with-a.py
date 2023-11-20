string = list(input())
leng = len(string)

string[1] = 'a'
string[leng-2] = 'a'

print("".join(string))