n=int(input())
ws=list(map(int,input().split()))
s1=ws[0]
s2=sum(ws[1:])
a=abs(s1-s2)
for t in ws[1:]:
    s1+=t
    s2-=t
    a=min(a,abs(s1-s2))
print(a)
