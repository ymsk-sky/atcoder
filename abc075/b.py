h,w=map(int,input().split())
s=[[c for c in input()] for _ in range(h)]
for i in range(h):
    for j in range(w):
        if s[i][j]=='#':
            continue
        c=0
        for a,b in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
            if i+a<0 or i+a>h-1 or j+b<0 or j+b>w-1:
                continue
            if s[i+a][j+b]=='#':
                c+=1
        s[i][j]=str(c)
for i in s:
    print(''.join(i))
