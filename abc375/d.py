from collections import defaultdict
s = input()
bef = defaultdict(int)
aft = defaultdict(int)
for c in s:
    aft[c] += 1
ans = 0
for c in s:
    aft[c] -= 1
    for a in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        ans += bef[a] * aft[a]
    bef[c] += 1
print(ans)
