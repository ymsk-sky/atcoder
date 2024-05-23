n = int(input())
al = list(map(int, input().split()))
bottom = 0
crt = 0
for a in al:
    crt += a
    bottom = min(bottom, crt)
ans = crt - bottom
print(ans)
