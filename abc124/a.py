a,b=map(int,input().split())
print(a+max(a-1,b) if a>b else b+max(a,b-1))
