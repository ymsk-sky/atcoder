n=int(input())
an=list(map(int,input().split()))
print(1/sum([1/a for a in an]))
