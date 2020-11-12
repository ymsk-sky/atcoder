"""
@ -> [atcoder]
"""
s=input()
t=input()
l='atcoder'
def lose():
    print('You will lose')
    exit()
for a,b in zip(s,t):
    if a==b:
        continue
    if a=='@':
        if b in l:
            continue
        else:
            lose()
    if b=='@':
        if a in l:
            continue
        else:
            lose()
    if a!=b:
        lose()
print('You can win')
