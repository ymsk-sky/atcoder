l=list(map(int,input().split()))
l.sort()
print('Yes' if l[2]-l[1]==l[1]-l[0] else 'No')
