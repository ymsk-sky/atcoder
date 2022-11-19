n = int(input())
al = list(map(int, input().split()))
q = int(input())
ans = []
d = -1
s = set()
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        # alのすべてにxを代入
        _, x = query
        d = x
        s = set()
    elif query[0] == 2:
        # al[i-1]にxを加える
        _, i, x = query
        if d >= 0 and not (i in s):
            al[i - 1] = d + x
            s.add(i)
        else:
            al[i - 1] += x
    else:
        # al[i-1]を出力
        _, i = query
        if d >= 0:
            if i in s:
                ans.append(al[i - 1])
            else:
                ans.append(d)
        else:
            ans.append(al[i - 1])

print(*ans, sep="\n")
