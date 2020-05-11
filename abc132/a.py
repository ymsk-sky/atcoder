d=dict()
for s in input():
    if not s in d:
        d[s]=1
    else:
        d[s]+=1
if len(d)==2:
    for v in d.values():
        if not v==2:
            print('No')
            exit()
else:
    print('No')
    exit()
print('Yes')
