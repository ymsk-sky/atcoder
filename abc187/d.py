"""
青木: A
高橋: B
高橋が演説でその町全員が高橋(B)となる
演説を行わなかった場合、
 - Aは青木(A)に投票
 - Bは投票しない
高橋(B)>青木(A)となるには何箇所演説が必要か
"""
n=int(input())
l=[list(map(int,input().split())) for _ in range(n)]
a_score=sum([a for a,_ in l])
b_score=0
scores=sorted([[a+b,a,b] for a,b in l],reverse=True,key=lambda x:(x[0],x[1],x[2]))
ans=0
for v,a,b in scores:
    a_score-=a
    b_score+=v
    ans+=1
    if a_score<b_score:
        break
print(ans)
"""
4
2 1 :3
2 2 :4
5 1 :6<-ここだけ演説
1 3 :4
10vs0(演説なし)
 -22-> 8vs4 -21-> vs 6vs7 寝返り数が多い方が得！
 -13-> 9vs4 -21-> vs 7vs7
どこからやるべきか？ - 得するところから順に必要分だけ

6
1 2
5 1
3 3
2 1
3 3
"""
