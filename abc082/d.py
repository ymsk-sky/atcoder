s = input()
X, Y = map(int, input().split())

xl = []
yl = []
cnt_t = 0
cnt_f = 0
def add():
    if cnt_t%2 == 0:
        xl.append(cnt_f)
    else:
        yl.append(cnt_f)
for c in s:
    if c == "F":
        cnt_f += 1
    else:
        add()
        cnt_f = 0
        cnt_t += 1
add()

xl.append(0)
yl.append(0)

dp_x = [set() for _ in range(len(xl))]
dp_x[0].add(xl[0])
for i in range(1, len(xl)):
    x = xl[i]
    for j in dp_x[i - 1]:
        dp_x[i].add(j + x)
        dp_x[i].add(j - x)

dp_y = [set() for _ in range(len(yl))]
dp_y[0].add(yl[0])
dp_y[0].add(-yl[0])
for i in range(1, len(yl)):
    y = yl[i]
    for j in dp_y[i - 1]:
        dp_y[i].add(j + y)
        dp_y[i].add(j - y)
if X in dp_x[-1] and Y in dp_y[-1]:
    print("Yes")
else:
    print("No")