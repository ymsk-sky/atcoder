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
scores=sorted([[2*a+b,a,b] for a,b in l],reverse=True,key=lambda x:(x[0],x[1],x[2]))
ans=0
for _,a,b in scores:
    a_score-=a
    b_score+=a+b
    ans+=1
    if a_score<b_score:
        break
print(ans)
"""
4
2 1 :3 (-1)
2 2 :4 (-2)
5 1 :6<-ここだけ演説 (-1)
1 3 :4 (-3)
10vs0(演説なし)
10差->4差 差を6縮められる
相手-a,自分+a+b よって差は2a+b
 -14-> 9vs5 差4!
 -22-> 8vs4 -21-> vs 6vs7 寝返り数が多い方が得！
 -13-> 9vs4 -21-> vs 7vs7
 -31-> 7vs4
どこからやるべきか？ - 得するところから順に必要分だけ
"""
