cs=[list(map(int,input().split())) for _ in range(3)]
a=[i-j for i,j in zip(cs[0],cs[1])]
b=[i-j for i,j in zip(cs[1],cs[2])]
print('Yes'if a[0]==a[1]==a[2] and b[0]==b[1]==b[2]else'No')
