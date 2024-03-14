n = int(input())
al = list(map(int, input().split()))
for i in range(n - 1):
    s, t = map(int, input().split())
    m = al[i] // s
    al[i + 1] += t * m
print(al[n - 1])
