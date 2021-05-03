s=input()
t=''
f=1  # reverse flag
for c in s:
    if c=='R':
        f*=-1
    else:
        if f==1:
            if len(t)>0 and c==t[-1]:
                t=t[:-1]
            else:
                t+=c
        else:
            if len(t)>0 and c==t[0]:
                t=t[1:]
            else:
                t=c+t
print(t if f==1 else t[::-1])
