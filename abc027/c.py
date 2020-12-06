n=int(input())
d=0
i=n
while i>0:
    d+=1
    i//=2
x=1
cnt=0
if d%2==1:
    while x<=n:
        x*=2
        x+=(cnt+1)%2
        cnt+=1
else:
    while x<=n:
        x*=2
        x+=cnt%2
        cnt+=1
print('Aoki' if cnt%2==1 else 'Takahashi')
