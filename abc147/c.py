from itertools import product
N=int(input())
shogens=[]
for _ in range(N):
    A=int(input())
    shogen=[list(map(int,input().split())) for _ in range(A)]
    shogens.append(shogen)
ans=0
for states in product((0,1),repeat=N):
    cnt=0
    for state,shogen in zip(states,shogens):
        if state==1:
            for x,y in shogen:
                if states[x-1]!=y:
                    break
            else:
                continue
            cnt+=1
    if cnt==sum(states):
        ans=max(ans,cnt)
print(ans)
