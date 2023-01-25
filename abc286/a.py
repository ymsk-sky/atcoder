n, p, q, r, s = map(int, input().split())
al = list(map(int, input().split()))

al[p-1:q], al[r-1:s] = al[r-1:s], al[p-1:q]
print(*al)