n=int(input())
l=list(map(int,input().split()))
finished=sum(l)
max_=max([sum(l[i:]) for i in range(1,n+1)])
if finished>=0:
    
