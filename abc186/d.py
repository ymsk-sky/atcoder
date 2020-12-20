n=int(input())
al=sorted(list(map(int,input().split())))
tmp=0
ans=0
for i,a in enumerate(al):
    ans+=i*a-tmp
    tmp+=a
print(ans)

"""
5
31 41 59 26 53
al: 26 31 41 53 59

0*26-0 0->26
1*31-26 26->57
"""
