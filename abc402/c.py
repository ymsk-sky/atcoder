INF = 1 << 60

n, m = map(int, input().split())
al_l = []
for _ in range(m):
    _, *al = list(map(int, input().split()))
    al_l.append(set(al))
bl = list(map(int, input().split()))

d = {b: INF for b in range(1, n + 1)}
for i, b in enumerate(bl):
    d[b] = i

cnt = [0] * n
for al in al_l:
    i = max([d[a] for a in al])
    if i == INF:
        continue
    cnt[i] += 1
for i in range(n - 1):
    cnt[i + 1] += cnt[i]
print(*cnt, sep="\n")
