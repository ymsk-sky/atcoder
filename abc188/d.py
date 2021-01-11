"""
a日目からb日目までc円かかるを
・(a-1)日目とa日目の間にc円上がるイベント
・b日目と(b+1)日目の間にc円下がるイベント
と考えてイベントをソートする
"""
N,C=map(int,input().split())
events=[]
for _ in range(N):
    a,b,c=map(int,input().split())
    events.append((a-1,c))
    events.append((b,-c))
events.sort()
ans=0
fee=0  # 現在のコスト
t=0  # 前回のイベントがあった日付
for x,y in events:
    if x!=t:  # イベント発生の日付が変わった場合
        # プライム価格(C)と現在コストの低いほうを期間分ansに追加
        ans+=min(C,fee)*(x-t)
        t=x
    # 現在のコストを更新
    fee+=y
print(ans)
