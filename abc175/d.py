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
print(scores)
"""
5 2
2 4 5 1 3
3 4 -10 -8 8
8

1: +4 -4 -1
2: -8 -5 -1
3: +8 -2 +6
4: +3 +7 -1
5: -10 -2 -12
"""
