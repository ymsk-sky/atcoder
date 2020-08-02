n=int(input())
m=0
a=1
for i in range(1,n+1):
    c=0
    j=i
    while 1:
        j/=2
        if j%1==0:
            c+=1
        else:
            break
    if m<c:
        m=c
        a=i
print(a)
