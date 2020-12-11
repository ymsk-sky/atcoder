n=int(input())  # alの個数
al=list(map(int,input().split()))  # a配列(この合計を出力する)
q=int(input())  # 操作回数
bcs=[list(map(int,input().split())) for _ in range(q)]  # q個の操作： bをcへ変換
dl=dict()
for a in al:
    if a in dl:
        dl[a]+=1
    else:
        dl[a]=1
for b,c in bcs:
    if b in dl:
        cnt_b=dl[b]  # bの個数
        dl[b]=0
        if c in dl:
            dl[c]+=cnt_b
        else:
            dl[c]=cnt_b
    ans=sum([k*v for k,v in dl.items()])
    print(ans)
