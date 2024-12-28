from itertools import combinations

n, k = map(int, input().split())
al = list(map(int, input().split()))

ans = 0
if k > n - k:
    s = 0  # 全体のxor
    for a in al:
        s ^= a
    for cl in combinations(al, n - k):
        tmp = s
        for a in cl:
            tmp ^= a
        ans = max(ans, tmp)
else:
    for cl in combinations(al, k):
        tmp = 0
        for a in cl:
            tmp ^= a
        ans = max(ans, tmp)

print(ans)
