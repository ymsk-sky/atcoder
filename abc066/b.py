s=input()
for i in range(len(s)-1, 1, -1):
    t=s[:i]
    l=len(t)
    if l%2!=0:
        continue
    if t[:l//2]==t[l//2:]:
        print(l)
        exit()
