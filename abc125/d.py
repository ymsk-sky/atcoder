n=int(input())
al=list(map(int,input().split()))
def do(i):
    al[i]*=-1
    al[i+1]*=-1
for i in range(n-1):
    a=al[i]
    b=al[i+1]
    if a>0 and b>0:
        pass
    elif a<=0 and b<=0:
        do(i)
    elif a<=0 and b>0:
        if abs(a)>b:
            do(i)
    elif a>0 and b<=0:
        if abs(b)>a:
            do(i)
    print('i =',i,':',al)
print(sum(al))
