n=int(input())
l=[input() for _ in range(n)]
b=l[0][-1]
for w in l[1:]:
    if l.count(w)>1 or not w[0]==b:
        print('No')
        exit()
    b=w[-1]
print('Yes')
