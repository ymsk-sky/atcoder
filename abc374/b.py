s = input()
t = input()
n = max(len(s), len(t))
s = s + "?" * (n - len(s))
t = t + "?" * (n - len(t))
ans = 0
for i in range(n):
    if s[i] != t[i]:
        ans = i + 1
        break
print(ans)
