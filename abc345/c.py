from collections import Counter

s = input()
n = len(s)
cnt = Counter(s)
ans = any([1 for v in cnt.values() if v > 1])
for i in range(n):
    c = s[i]
    m = n - i - cnt[c]
    ans += m
    cnt[c] -= 1
print(ans)
