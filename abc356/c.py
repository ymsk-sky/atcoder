n, m, k = map(int, input().split())
l = []
for _ in range(m):
    c, *al, r = input().split()
    c = int(c)
    al = [int(a) for a in al]
    l.append((c, al, r))
ans = 0
for state in range(1 << n):
    ok = True
    for c, al, r in l:
        # 正しい鍵の本数をカウント
        cnt = 0
        for a in al:
            if (state >> (a - 1)) & 1:
                cnt += 1
        if (r == "o" and cnt >= k) or (r == "x" and cnt < k):
            continue
        else:
            ok = False
    if ok:
        ans += 1
print(ans)
