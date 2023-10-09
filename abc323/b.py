n = int(input())
l = []
for i in range(1, n + 1):
    s = input()
    l.append((s.count("o"), -i))
l.sort(reverse=True)
print(*[-i for _, i in l])