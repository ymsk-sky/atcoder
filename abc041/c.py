n=int(input())
l=list(map(int,input().split()))
for _,i in sorted([[a,i] for i,a in enumerate(l)],reverse=True):
    print(i+1)
