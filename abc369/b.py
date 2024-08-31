n = int(input())
ans = 0
r = -1
l = -1
for _ in range(n):
    a, s = input().split()
    a = int(a)
    if s == "R":
        if r == -1:
            pass
        else:
            ans += abs(r - a)
        r = a
    else:
        if l == -1:
            pass
        else:
            ans += abs(l - a)
        l = a
print(ans)
