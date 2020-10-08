txa,tya,txb,tyb,t,v=map(int,input().split())
a=t*v
n=int(input())
l=[list(map(int,input().split())) for _ in range(n)]
for x,y in l:
    d1=((txa-x)**2+(tya-y)**2)**(1/2)
    d2=((x-txb)**2+(y-tyb)**2)**(1/2)
    if d1+d2<=a:
        print('YES')
        exit()
print('NO')


"""
1 1 8 2 2 4
1
4 5

1 1 8 2 2 6
1
4 5

1 1 8 2 2 5
1
4 5

7 7 1 1 3 4
3
8 1
1 7
9 9
"""
