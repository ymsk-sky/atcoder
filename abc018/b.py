s=input()
n=int(input())
for _ in range(n):
    l,r=map(int,input().split())
    t=''.join(reversed(s[l-1:r]))
    s=s[:l-1]+t+s[r:]
print(s)
