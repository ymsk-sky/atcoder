"""
1<=i<=n-1のiを選択後、al[i],al[i+1]に-1をかける
任意の回数上記を行なった後のalの合計の最大を求める

5
10 -4 -8 -11 3
30
"""
n=int(input())
l=list(map(int,input().split()))
def do(i):
    al[i]*=-1
    al[i+1]*=-1
ans=-float('inf')
for al in [l, l[::-1]]:
    for i in range(n-1):
        a=al[i]
        b=al[i+1]
        if a>0 and b>0:
            pass
        elif a<=0 and b<=0:
            do(i)
        elif a<=0 and b>0:
            if abs(a)>=b:
                do(i)
        elif a>0 and b<=0:
            if abs(b)>a:
                do(i)
    ans=max(ans,sum(al))
print(ans)
