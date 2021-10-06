s=[c for c in input()]
t=[c for c in input()]
if s==t:
    print('Yes')
    exit()
for i in range(len(s)-1):
    a=s.copy()
    si=s[i]
    sj=s[i+1]
    a[i]=sj
    a[i+1]=si
    if a==t:
        print('Yes')
        exit()
print('No')
