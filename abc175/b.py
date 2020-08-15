n=int(input())
l=list(map(int,input().split()))
s=0
for i,a in enumerate(l):
    for j,b in enumerate(l[i+1:]):
        for c in l[i+j+1:]:
            if a==b or b==c or c==a:
                continue
            if a+b>c and b+c>a and c+a>b:
                s+=1
print(s)
