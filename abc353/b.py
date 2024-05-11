n, k = map(int, input().split())
al = list(map(int, input().split()))
cnt = 0
crt = 0
for a in al:
    if crt + a <= k:
        crt += a
    else:
        crt = a
        cnt += 1
cnt += 1
print(cnt)
