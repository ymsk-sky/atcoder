n=int(input())
l=set(list(map(int,input().split())))
max_=max(l)
min_=min(l)
while len(l)>1:
    l.remove(max_)
    l.add(max_-min_)
    max_=max(l)
    min_=min(l)
print(min_)
