n,m,x,y=map(int,input().split())
xs=list(map(int,input().split()))
ys=list(map(int,input().split()))
x_=max(xs)
y_=min(ys)
for z in range(x_+1,y_+1):
    if x<z<=y:
        print('No War')
        exit()
print('War')
