n, d, p = map(int, input().split())
fl = list(map(int, input().split()))
fl.sort(reverse=True)
ans = sum(fl)
tmp = ans
for i in range(n):
    tmp -= fl[i]
    if (i + 1)%d == 0:
        tmp += p
        ans = min(ans, tmp)
ans = min(ans, -(-n//d)*p)
print(ans)
