N, X = map(int,input().split())
Al = list(map(int,input().split()))
sl=[0] * N
sl[X - 1] = 1
while 1:
    A = Al[X - 1]
    if sl[A - 1] == 1:
        break
    else:
        sl[A - 1] = 1
        X = A
print(sum(sl))
