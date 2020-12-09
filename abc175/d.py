n,k=map(int,input().split())
ps=list(map(int,input().split()))  # 1~nの順列
cs=list(map(int,input().split()))  # 1~nに到着時のスコア
scores=[[] for _ in range(n)]
for i in range(n):
    j=ps[i]-1  # 次のインデックス
    tmp=0  # 移動前のスコア
    while 1:
        c=cs[j]  # 移動時の加算スコア
        tmp+=c
        scores[i].append(tmp)  # スコアを更新
        if i==j:
            break
        j=ps[j]-1  # 次のインデックスを更新
ans=-float('inf')
for score in scores:
    l=len(score)  # 一周の長さ
    if l>=k:
        ans=max(ans,max(score[:k]))
    else:
        max_val=max(score)
        num=k//l  # 繰り返し回数
        mod=k%l  # 端数部分
        tail=score[-1]  # 繰り返すごとに増える数
        if tail>0:  # 最大まで繰り返す
            max_val+=tail*(num-1)
            ans=max(ans,max_val,max(score[:mod])+tail*num)
        else:  # １回目で終わらせる
            ans=max(ans,max_val)
print(ans)
"""
5 2
2 4 5 1 3
3 4 -10 -8 8
8

1: +4 -4 -1 | +3 -5 -2 | +2 -6 -3
2: -8 -5 -1
3: +8 -2 | +6 -4 | +4 -6
4: +3 +7 -1
5: -10 -2

+1 -2 +2 | +3 0 +4 | +5 +2 +6
"""
