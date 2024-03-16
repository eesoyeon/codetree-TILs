n, k, T = input().split()
n, k = int(n), int(k)
words = [input() for _ in range(n)]
ans = []

words.sort()
for word in words:
    if T in word:
        ans.append(word)

print(ans[k-1])