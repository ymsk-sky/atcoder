n, m = map(int, input().split())
cl = input().split()
dl = input().split()
pl = list(map(int, input().split()))

dict_ = {}
for i in range(m):
    dict_[dl[i]] = pl[i + 1]

p = pl[0]

ans = 0
for c in cl:
    if c in dict_:
        ans += dict_[c]
    else:
        ans += p

print(ans)
