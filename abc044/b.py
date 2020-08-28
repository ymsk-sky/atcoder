w=input()
d={}
for c in w:
    if c in d:
        d[c]+=1
    else:
        d[c]=1
for k in d:
    if d[k]%2!=0:
        print('No')
        exit()
print('Yes')
