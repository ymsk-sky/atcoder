n, k = map(int, input().split())
al = list(map(int, input().split()))

bl = sorted(al)
ac = 0
for i in range(n):
    a = bl[i] - ac
    remain = k // (n - i)
    if remain <= a:
        ac += remain
        k -= remain * (n - i)
        break
    else:
        ac += a
        k -= a * (n - i)

ans = [max(0, a - ac) for a in al]
if k > 0:
    for i in range(n):
        if ans[i] > 0:
            ans[i] -= 1
            k -= 1
        if k == 0:
            break
print(*ans)