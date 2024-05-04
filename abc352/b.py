s = input()
t = input()
m = len(t)
ans = []
i = 0
for j in range(m):
    if t[j] == s[i]:
        ans.append(j + 1)
        i += 1
print(*ans)
