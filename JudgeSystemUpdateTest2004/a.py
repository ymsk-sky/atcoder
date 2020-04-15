s,l,r=map(int,input().split())
if l<s<r:print(s)
else:print(l if abs(s-l)<abs(s-r) else r)
