# 間違い & 提出:LTE

k=int(input())
ls=[1,2,3,4,5,6,7,8,9,10,11,12]
i=21
while len(ls)<10**5:
    si=str(i)
    for s,n in zip(si, si[1:]):
        if not abs(int(s)-int(n))<=1:
            break
        if n==si[-1]:
            ls.append(i)
    i+=1
print(ls[k-1])
