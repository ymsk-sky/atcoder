n=int(input())
d=dict({i:0 for i in range(1,n+1)})
for s in range(3,201):
    for x in range(1,s+1-2):
        for y in range(1,s+1-x-1):
            z=s-x-y
            v=x**2+y**2+z**2+x*y+y*z+z*x
            if not v in d:
                continue
            d[v]+=1
for k in d.keys():
    print(d[k])
