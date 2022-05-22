N = int(input())
Sl = list(map(int, input().split()))
p = set([4*a*b + 3*a + 3*b for a in range(1, 334) for b in range(1, 334)])

ans = 0
for S in Sl:
    if S in p:
        pass
    else:
        ans+=1

print(ans)
