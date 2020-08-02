n=int(input())
cs=input()
ss=sorted(cs)
wr=0
for x,y in zip(cs,ss):
    if x=='W' and y=='R':
        wr+=1
print(wr)
