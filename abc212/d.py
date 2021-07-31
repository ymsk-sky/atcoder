import heapq
q=int(input())
alp=0  # 袋内すべてに値を足すのではなくそれ以降の値から引く(基準点を下げる)
bl=[]  # balls
heapq.heapify(bl)
for _ in range(q):
    l=list(map(int,input().split()))
    p=l[0]
    if p==1:  # 袋にxを入れる
        x=l[1]-alp
        heapq.heappush(bl,x)
    elif p==2:  # 袋内のボール全てにxを足す
        x=l[1]
        alp+=x
    else:  # 最小を取り出し出力
        ans=heapq.heappop(bl)
        ans+=alp
        print(ans)
