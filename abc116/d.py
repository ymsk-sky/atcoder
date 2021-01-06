"""
n個からk個を選択
t,d: ネタ,美味しさ
満足ポイントの最大値を求める
ネタt -> tの種類の二乗
美味しさd -> 和
の和
M = t*t + (d1,d2,...)
"""
n,k=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(n)]
