n = int(input())
s = input()
ans = 0
for i in range(n - 2):
    ans += s[i] == s[i + 2] == "#" and s[i + 1] == "."
print(ans)
