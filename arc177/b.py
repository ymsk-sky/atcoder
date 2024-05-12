from itertools import groupby

n = int(input())
s = input()
gl = [(k, len(list(v))) for k, v in groupby(s)]
ans = []
length = n
while gl:
    k, m = gl.pop()
    if k == "1":
        ans.append("A" * length)
        ans.append("B" * (length - m))
    length -= m

print(sum([len(an) for an in ans]))
print("".join(ans))

"""
1<=n<=30

5
01100
A -> 最左の0->1
B -> 最左の1->0

"""