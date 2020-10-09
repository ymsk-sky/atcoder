n=int(input())
l=set([int(input()) for _ in range(n)])
print(max(l-{max(l)}))
