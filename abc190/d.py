n=int(input())
while n%2==0:
    n//=2
sq=int(n**(1/2))
cnt=0
for i in range(1,sq+1):
    if n%i==0:
        cnt+=1
ad=1 if sq*sq==n else 0
tmp=cnt*2-ad
print(tmp*2)
