n,k=map(int,input().split())
abl=[list(map(int,input().split())) for _ in range(n)]
abl.sort()
ans=0
crt=k  # 所持金
pos=0  # 現在地
for a,b in abl:
    if crt>=a-pos:  # 次(最も近い村)に到着できるか
        crt-=(a-pos)  # 移動した分消費
        crt+=b  # 到着時に受け取る分回復
        pos=a
    else:  # 到着できない場合
        break
ans=crt+pos
print(ans)
