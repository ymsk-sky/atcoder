n, m = map(int, input().split())
sl = [input() for _ in range(n)]
tl = [input() for _ in range(m)]
ans = 0
for s in sl:
    c = s[3:]
    for t in tl:
        if c == t:
            ans += 1
            break
print(ans)