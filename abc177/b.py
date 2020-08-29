s=input()
t=input()
tl=len(t)
m=0
for i in range(len(s)-tl+1):
    c=0
    for x,y in zip(t,s[i:i+tl]):
        if x==y:
            c+=1
    m=max(m,c)
print(tl-m)
