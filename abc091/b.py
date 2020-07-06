n=int(input())
s=[input()for _ in range(n)]
m=int(input())
t=[input()for _ in range(m)]
a=0
for w in set(s):
    a=max(a,s.count(w)-t.count(w))
print(a)
