n=int(input())
s=list(map(int,input().split()))
ans=-float('inf')
for i in range(n):  # takahashi select
    max_t=-float('inf')
    max_a=-float('inf')
    for j in range(n):  # aoki select
        if i==j:
            continue
        if i<j:
            t=s[i:j+1]
        else:
            t=s[j:i+1]
        point_t=sum(t[0::2])
        point_a=sum(t[1::2])
        if point_a>max_a:
            max_a=point_a
            max_t=point_t
    ans=max(ans,max_t)
print(ans)
