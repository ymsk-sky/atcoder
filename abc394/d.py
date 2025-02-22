from collections import deque

s = input()
que = deque()
for c in s:
    if c == ")" or c == "]" or c == ">":
        if len(que) > 0:
            bef = que.pop()
            if bef == "(" and c == ")":
                continue
            if bef == "[" and c == "]":
                continue
            if bef == "<" and c == ">":
                continue
        que.append(c)
    else:
        que.append(c)
print("Yes" if len(que) == 0 else "No")
