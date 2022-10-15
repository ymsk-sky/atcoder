from collections import deque

q = int(input())

ky = 0
A_dict = dict()
A_dict[ky] = deque()

ans = []
note = dict()
for _ in range(q):
    query = input().split()
    q0 = query[0]
    if q0 == "ADD":
        x = query[1]
        A_dict[ky].append(x)
    elif q0 == "DELETE":
        if len(A_dict[ky]) > 0:
            A_dict[ky].pop()
    elif q0 == "SAVE":
        y = query[1]
        note[y] = ky
    elif q0 == "LOAD":
        z = query[1]
        if z in note:
            ky = note[z]
        else:
            ky = z
            A_dict[ky] = deque()
    if len(A_dict[ky]) > 0:
        a = A_dict[ky].pop()
        ans.append(a)
        A_dict[ky].append(a)
    else:
        ans.append(-1)

print(*ans)
