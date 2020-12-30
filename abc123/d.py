x,y,z,k=map(int,input().split())
al=sorted(list(map(int,input().split())))
bl=sorted(list(map(int,input().split())))
cl=sorted(list(map(int,input().split())))
dl=sorted([a+b for a in al for b in bl],reverse=True)[:k]
el=sorted([c+d for c in cl for d in dl],reverse=True)
for e in el[:k]:
    print(e)
"""
2 2 2 8
4 6
1 5
3 8
"""
