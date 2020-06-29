h,w=map(int,input().split())
s=[input() for _ in range(h)]
for i in range(h):
    for j in range(w):
        if s[i][j]=='.':
            continue
        if not i==0:
            if s[i-1][j]=='#':
                continue
        if not j==0:
            if s[i][j-1]=='#':
                continue
        if not i==h-1:
            if s[i+1][j]=='#':
                continue
        if not j==w-1:
            if s[i][j+1]=='#':
                continue
        print('No')
        exit()
print('Yes')
