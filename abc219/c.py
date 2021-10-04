x=input()
n=int(input())
a='abcdefghijklmnopqrstuvwxyz'
d={i:j for i,j in zip(x,a)}  # 対応表
sl=[]
for _ in range(n):
    s=input()
    t=''.join([d[c] for c in s])
    sl.append((t,s))
sl.sort()
for s in sl:
    print(s[1])
