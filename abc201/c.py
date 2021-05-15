s=input()
o=[]
x=[]
q=[]
for i,c in enumerate(s):
    if c=='o':
        o.append(str(i))
    if c=='x':
        x.append(str(i))
    if c=='?':
        q.append(str(i))
if len(o)==4:
    print(24)
    exit()
if len(o)>4:
    print(0)
    exit()
if len(o)==0:
    print(len(q)**4)
    exit()
cnt=0
for i in range(10000):
    S=str(i).zfill(4)
    lo=[1 for c in o if c in S]
    lx=[1 for c in x if c in S]
    if sum(lo)==len(o) and sum(lx)==0:
        cnt+=1
print(cnt)
