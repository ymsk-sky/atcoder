from math import factorial
def comb(n,r):
    return factorial(n)//(factorial(r)*factorial(n-r))
a,b,k=map(int,input().split())
ans=''
while a>0 and b>0:
    c=comb(a-1+b,a-1)  # 先頭が'a'の個数
    if k<=c:
        ans+='a'
        a-=1
    else:
        ans+='b'
        b-=1
        k-=c
ans+='a'*a
ans+='b'*b
print(ans)
