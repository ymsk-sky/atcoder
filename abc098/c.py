"""思考
初期状態を全員西向きにする => 東向きの人数 が変化数(答え)
この状態からリーダーの位置を右にずらしていく
"""
n=int(input())
s=input()
ans=float('inf')
rs=s.count('E')  # リーダーより右側(東側)の"変化人数"
ls=0  # リーダーより左側(西側)の"変化人数"
for c in s:
    cnt=rs+ls
    if c=='E':
        cnt-=1
        rs-=1
    else:
        ls+=1
    ans=min(ans,cnt)
print(ans)
"""
5
WEEWW
E(East:東[右])
W(West:西[左])

1 0EEWW -> 0WWWW = 2
2 W0EWW -> E0WWW = 1
3 WE0WW -> EE0WW = 1
4 WEE0W -> EEE0W = 1
5 WEEW0 -> EEEE0 = 2
"""
