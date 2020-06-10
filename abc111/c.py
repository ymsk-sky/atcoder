from collections import Counter
n=int(input())
vs=list(map(int,input().split()))
xs=vs[0::2]
ys=vs[1::2]
cx=Counter(xs).most_common()
cy=Counter(ys).most_common()
if len(cx)==1:
    cx.append((0,0))
if len(cy)==1:
    cy.append((-1,0))
if not cx[0][0]==cy[0][0]:
    print(len(xs)-cx[0][1]+len(ys)-cy[0][1])
else:
    mx=len(xs)-cx[1][1]+len(ys)-cy[0][1]
    my=len(xs)-cx[0][1]+len(ys)-cy[1][1]
    print(min(mx,my))
