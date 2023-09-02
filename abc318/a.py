n, m, p = map(int, input().split())
if n - m < 0:
    print(0)
    exit()
ans = 1
n -= m
ans += n//p
print(ans)
