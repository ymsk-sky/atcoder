n=int(input())
ss=[input() for _ in range(n)]
d1=set()
d2=set()
for s in ss:
    if s[0]=='!':
        d2.add(s[1:])
    else:
        d1.add(s)
d=d1&d2
if len(d)>0:
    print(list(d)[0])
else:
    print('satisfiable')
