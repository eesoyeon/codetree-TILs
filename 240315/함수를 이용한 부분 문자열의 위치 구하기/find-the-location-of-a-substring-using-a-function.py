a = input()
b = input()

def find_index():
    if a.index(b):
        return a.index(b)
    else:
        return -1
    
ans = find_index()
print(ans)