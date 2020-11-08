n=input()
k=len(n)
m1=0
m2=0
for v in n:
    v=int(v)
    if v%3==0:  # 3,6,9
        continue
    elif v%3==1:  # 1,4,7
        m1+=1
    else:  # 2,5,8
        m2+=1
d1=abs(m1-m2)
m1%=3
m2%=3
d2=abs(m1-m2)
ans=min(d1,d2)
print(ans if ans!=k else -1)
