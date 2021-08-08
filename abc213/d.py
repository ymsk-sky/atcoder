n=int(input())
abl=[list(map(int,input().split())) for _ in range(n-1)]
visited=[0]*(n+1)  # 1なら済み
visited[1]=1
graph=[[] for _ in range(n+1)]  # graph[X]: Xから行ける都市一覧
for a,b in abl:
    graph[a].append(b)
    graph[b].append(a)
graph=[sorted(l) for l in graph]  # 小さい順に調べるためソート
ans=[1]
pos=1  # 現在地
back=1  # 戻る場合の戻る個数
while 1:
    flag=0
    for r in graph[pos]:  # r: 次の都市
        if visited[r]==0:  # 未踏
            pos=r
            ans.append(r)
            visited[r]=1
            flag=1
            back=1
            break
        else:  # 既に行ったことある
            pass
    # 行ける都市がない場合
    if flag==0:
        if pos==1:
            break
        else:
            pos=ans[::-1][back]
            ans.append(pos)
            back+=2
ans=[str(i) for i in ans]
print(' '.join(ans))
