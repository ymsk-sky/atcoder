n=int(input())
moves=[0]+[int(input()) for _ in range(5)]
holds=[n]+[0]*5
t=0
while 1:
    for i in range(5,0,-1):
        if holds[i-1]-moves[i]>=0:
            trans=moves[i]
        else:
            trans=holds[i-1]
        holds[i-1]-=trans
        holds[i]+=trans
    t+=1
    if holds[-1]==n:
        break
print(t)
