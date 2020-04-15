n=int(input())
xcs=[list(input().split()) for _ in range(n)]
rs,bs=[[int(x), c] for x,c in xcs if c=='R'],[[int(x), c] for x,c in xcs if c=='B']
rs.sort()
bs.sort()
print(*[r[0] for r in rs],*[b[0] for b in bs])
