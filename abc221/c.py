from itertools import permutations
n=input()
ans=0
l=len(n)
for p in permutations(n):
    for i in range(1,l):
        a=''.join(p[:i])
        b=''.join(p[i:])
        if a[0]=='0' or b[0]=='0':
            continue
        ans=max(ans,int(a)*int(b))
print(ans)
