n = int(input())
al = list(map(int, input().split()))
s = sum(al)
l = s//n
r = -(-s//n)
p = 0
m = 0
for a in al:
    if a <= l:
        m += l - a
    else:
        p += a - r
print(max(p, m))
