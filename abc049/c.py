s=input()
l=['dreamer','eraser','dream','erase']
t=''
a=0
for c in s[::-1]:
    t=c+t
    if t in l:
        a+=len(t)
        t=''
print('YES'if a==len(s)else'NO')
