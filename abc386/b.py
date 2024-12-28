s = input()
n = len(s)
ans = 0
i = 0
while i < n:
    x = s[i]
    if x == "0" and i < n - 1 and s[i + 1] == "0":
        i += 1
    ans += 1
    i += 1
print(ans)
