n, t = map(int, input().split())
cl = list(map(int, input().split()))
rl = list(map(int, input().split()))
if not t in cl:
    t = cl[0]
ans = val = -1
for i in range(n):
    c = cl[i]
    r = rl[i]
    if c == t:
        if r > val:
            val = r
            ans = i + 1
print(ans)
