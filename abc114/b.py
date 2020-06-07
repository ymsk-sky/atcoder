s=input()
m=float('inf')
for i in range(len(s)-2):
    v=int(s[i:i+3])
    m=min(m,abs(753-v))
print(m)
