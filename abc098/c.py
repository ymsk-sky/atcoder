n=int(input())
s=input()
ans=float('inf')
es=s.count('E')
changed=0
for c in s:
    cnt=es
    if c=='E':
        cnt-=1
    else:
        changed+=1
    ans=min(ans,cnt)
print(ans)
"""
5
WEEWW
E(East:東[右])
W(West:西[左])

1 0EEWW -> 0WWWW = 2
2 W0EWW -> E0WWW = 1
3 WE0WW -> EE0WW = 1
4 WEE0W -> EEE0W = 1
5 WEEW0 -> EEEE0 = 2
"""
