N = int(input())
Tl = []
Kl = []
Al = []
for _ in range(N):
    T, K, *A = list(map(int,input().split()))
    Tl.append(T)
    Kl.append(K)
    Al.append(A)
ans = 0
fin=set([])

def f(i):
    global ans
    if i in fin:
        return
    fin.add(i)
    ans += Tl[i]
    for a in Al[i]:
        f(a - 1)

f(N - 1)

print(ans)