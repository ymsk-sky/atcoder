x,k,d=map(int,input().split())
if k*d<abs(x):
    print(abs(x)-k*d)
    exit()
n=abs(x)-abs(x)//d*d # 残りの距離
m=k-abs(x)//d  # 余った回数
if m%2==0:
    print(n)
else:
    print(abs(n-d))
