"""
1<=i<=n-1のiを選択後、al[i],al[i+1]に-1をかける
任意の回数上記を行なった後のalの合計の最大を求める
5
10 -4 -8 -11 3
30
"""
n=int(input())
al=list(map(int,input().split()))
cnt=0
for a in al:
    if a<0:
        cnt+=1
    elif a==0:
        cnt=-1  # 0が存在
        break
if cnt==0:  # 負の数が存在しない
    ans=sum(al)
elif cnt==-1 or cnt%2==0:  # 0が存在または負の数が偶数
    ans=sum([abs(a) for a in al])
else:  # 負の数が奇数=1つを残して他は正にできる
    min_=min([abs(a) for a in al])
    ans=sum([abs(a) for a in al])-2*min_
print(ans)
"""
x,y(x<y)のときAx,Ayを-Ax,-Ayにできる
x=1,y=5のときy-x=4回(i=1,2,3,4:i=x,x+1,...,y-1)操作を繰り返す
 +10  -4  -8  -11  +3
[-10  +4] -8  -11  +3
 -10 [-4  +8] -11  +3
 -10  -4 [-8  +11] +3
 -10  -4  -8 [-11  -3]
 """
