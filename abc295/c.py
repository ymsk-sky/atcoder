from collections import Counter

n = int(input())
al = list(map(int, input().split()))
c = Counter(al)
ans = 0
for k in c:
    ans += c[k]//2
print(ans)
