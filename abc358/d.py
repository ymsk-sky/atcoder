n, m = map(int, input().split())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))
al.sort()
bl.sort()

ans = 0
j = 0
for a in al:
    if a >= bl[j]:
        ans += a
        j += 1
    if j >= m:
        break
else:
    print(-1)
    exit()
print(ans)
