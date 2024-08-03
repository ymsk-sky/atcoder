n, m = map(int, input().split())
al = list(map(int, input().split()))
ok = 0
ng = 10**20
while ng - ok > 1:
    x = (ok + ng) // 2
    s = sum([min(a, x) for a in al])
    if s > m:
        ng = x
    else:
        ok = x
print("infinite" if ok == 99999999999999999999 else ok)
