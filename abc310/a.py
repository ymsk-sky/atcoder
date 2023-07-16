n, p, q = map(int, input().split())
dl = list(map(int, input().split()))
print(min(p, q + min(dl)))
