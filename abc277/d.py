n, m = map(int, input().split())
al = list(map(int, input().split()))
al = [a for a in al if a != 0]
if len(al) < 2:
    print(0)
    exit()

al.sort()
ans = sum(al)

l = []
bef = al[0]
tmp = [bef]
for a in al[1:]:
    if bef == a or bef + 1 == a:
        tmp.append(a)
    else:
        l.append(tmp)
        tmp = [a]
    bef = a
if tmp:
    l.append(tmp)

if len(l) == 1:
    print(0)
    exit()

if l[0][0] == 1 and l[-1][-1] == m - 1:
    tmp = l.pop()
    l[0] = l[0] + tmp

x = 0
for s in l:
    x = max(x, sum(s))

print(ans - x)

"""
1<=n<=2*10**5
2<=m<=10**9
0<=a<m

9 7
3 0 2 5 5 3 0 6 3
11

2 3 3 3 5 5 6

最長の連続した部分を消す
"""
