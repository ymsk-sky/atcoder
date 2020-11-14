"""
上にh-1, 左にw-1移動の組み合わせ
-> h+w-2回の内、h-1回移動する方法を求めればよい
(h+w-2)C(h-1) : 組み合わせ = (h+w-2)!/((h-1)!(w-1)!)
そのまま計算はオーダーオーバー
aのb乗をpで割った余りを計算する
"""
w,h=map(int,input().split())
m=10**9+7
def d(a,b,p):
    if b==0:
        return 1
    if b%2==0:
        t=d(a,b//2,p)
        return (t*t)&p
    else:
        return (a*d(a,b-1,p))%p
print(d(h+w-2,h-1,m))
