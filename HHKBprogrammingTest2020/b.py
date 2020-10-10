h,w=map(int,input().split())
l=[input() for _ in range(h)]
c=0
for i in range(h):
    for j in range(w):
        if l[i][j]=='.':
            if j!=w-1:
                if l[i][j+1]=='.':
                    c+=1
            if i!=h-1:
                if l[i+1][j]=='.':
                    c+=1
print(c)
