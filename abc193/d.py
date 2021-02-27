def calc(l,n):
    l=l[:-1]+str(n+1)
    sum_=0
    for i in range(1,10):
        cnt=l.count(str(i))
        sum_+=i*(10**cnt)
    return sum_
k=int(input())
s=input()
t=input()
nokori=[k]*9
for c1,c2 in zip(s[:-1],t[:-1]):
    nokori[int(c1)-1]-=1
    nokori[int(c2)-1]-=1
won=0
lost=0
for i in range(9):
    if nokori[i]==0:
        continue
    for j in range(9):
        if i==j and nokori[j]==1:
            continue
        elif nokori[j]==0:
            continue
        t_score=calc(s,i)
        a_score=calc(t,j)
        if t_score>a_score:
            tmp=nokori[i]*nokori[j] if i!=j else nokori[i]*(nokori[j]-1)
            won+=tmp
        else:
            tmp=nokori[i]*nokori[j] if i!=j else nokori[i]*(nokori[j]-1)
            lost+=tmp
print(won/(won+lost))
