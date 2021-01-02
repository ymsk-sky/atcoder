a,b=map(str,input().split())
print(max(sum([int(v) for v in a]),sum([int(v) for v in b])))
