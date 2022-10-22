n = int(input())
al = list(map(int, input().split()))

l = [0] * (2 * n + 2)
l[1] = 0
for i in range(1, n + 1):
    a = al[i - 1]
    num = l[a]
    l[2 * i] = num + 1
    l[2 * i + 1] = num + 1

for ans in l[1:]:
    print(ans)

"""
4
1 3 5 2

0
1
1
2
2
3
3
2
2

番号al[i-1]が分裂し2*i, 2*i + 1 番と番号をつけた

i=1: 1 -> 2,3
i=2: 3 -> 4,5 
i=3: 5 -> 6,7
i=4: 2 -> 8,9
"""