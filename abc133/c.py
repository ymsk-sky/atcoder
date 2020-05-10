l,r=map(int,input().split())
a=range(l,r+1)
m=float('inf')
for i in a:
    for j in range(i+1,r+1):
        m=min(m,(i*j)%2019)
        if m==0:
            print(0)
            exit()
print(m)
