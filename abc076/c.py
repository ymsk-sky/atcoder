sd=[c for c in input()]
t=[c for c in input()]
tl=len(t)
for i in range(len(sd)-tl,-1,-1):
    s=sd.copy()
    m=sd[i:i+tl]
    for j in range(tl):
        if m[j]=='?':
            s[i+j]=t[j]
        elif m[j]==t[j]:
            pass
        else:
            break
    if s[i:i+tl]==t:
        print(''.join(['a' if c=='?' else c for c in s]))
        exit()
print('UNRESTORABLE')
