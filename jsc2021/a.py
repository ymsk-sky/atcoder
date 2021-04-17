x,y,z=map(int,input().split())
v=y/x*z
print(int(v)-1 if v==int(y/x*z) else int(v))
