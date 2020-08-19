n=int(input())
s=input()
m=0
t=0
for c in s:
    if c=='I':
        t+=1
    elif c=='D':
        t-=1
    m=max(m,t)
print(m)
