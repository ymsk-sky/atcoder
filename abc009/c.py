from itertools import permutations
n,k=map(int,input().split())
s=input()
for t in permutations(sorted(s)):
    cnt=0
    for a,b in zip(s,t):
        if a==b:
            pass
        else:
            cnt+=1
    if cnt<=k:
        print(''.join(list(t)))
        exit()
