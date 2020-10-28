s=input()
t=input()
d={}
for x,y in zip(s,t):
    if (x in d) and d[x]!=y:
        print('No')
        exit()
    d[x]=y
if len(d)==len(set(d.values())):
    print('Yes')
else:
    print('No')
