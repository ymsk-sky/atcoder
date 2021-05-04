n=int(input())
l=[list(map(int,input().split())) for _ in range(n)]
def check(X):
    s=set()
    for a in l:
        sum_=0
        for i,v in enumerate(a):
            if v>=X:
                sum_+=1<<i
        s.add(sum_)
    for x in s:
        for y in s:
            for z in s:
                if x|y|z==31:
                    return True
    return False
ok=0
ng=10**9+1
while ng-ok>1:
    cen=(ok+ng)//2
    if check(cen):
        ok=cen
    else:
        ng=cen
print(ok)
