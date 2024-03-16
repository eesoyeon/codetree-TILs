n, k, T = input().split()
n, k = int(n), int(k)
# words = [input() for _ in range(n)]
# ans = []

# words.sort()
# for word in words:
#     if word[:len(T)] == T:
#         ans.append(word)

# print(ans[k-1])


def starts_with(a, b):
    if len(a) < len(b):
        return False
    return a[:len(b)] == b

words = []
for _ in range(n):
    word = input()
    if starts_with(word, T):
        words.append(word)

words.sort()
print(words[k-1])