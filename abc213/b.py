n=int(input())
al=list(map(int,input().split()))
al=[(a,i) for i,a in enumerate(al,start=1)]
al.sort(reverse=True)
print(al[1][1])
