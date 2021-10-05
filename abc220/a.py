a,b,c=map(int,input().split())
for i in range(1,1001):
    if a<=c*i<=b:
        print(c*i)
        exit()
print(-1)
