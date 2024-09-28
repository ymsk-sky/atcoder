s = input()
ans = 0
i = s.index("A")
for c in "BCDEFGHIJKLMNOPQRSTUVWXYZ":
    j = s.index(c)
    ans += abs(i - j)
    i = j
print(ans)
