l=[input() for _ in range(5)]
i=0
m=9
for s in l:
    s=int(s[-1])
    if s==0:
        i+=1
        continue
    m=min(m,s)
a=0
for s in l:
    a+=(int(s)+9)//10*10
print(a if i==len(l) else a-10+m)
