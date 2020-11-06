from collections import Counter
n=int(input())
l=[input() for _ in range(n)]
c=Counter(l)
print(c.most_common()[0][0])
