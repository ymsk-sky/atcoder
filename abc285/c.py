s = input()
n = len(s)
ans = 0
for i in range(n):
    c = s[i]
    x = ord(c) - 64
    ans += x * 26**(n - i - 1)
print(ans)
