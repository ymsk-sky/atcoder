s, t = input().split()
if s == "sick":
    if t == "sick":
        ans = 1
    else:
        ans = 2
else:
    if t == "sick":
        ans = 3
    else:
        ans = 4
print(ans)
