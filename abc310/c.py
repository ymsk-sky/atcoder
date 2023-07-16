n = int(input())
sl = set()
ans = 0
for _ in range(n):
    s = input()
    t = s[::-1]
    if (not s in sl) and (not t in sl):
        sl.add(s)
        ans += 1
print(ans)
