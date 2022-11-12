n = int(input())
sl = [input() for _ in range(n)]
if len(sl) ==len(set(sl)):
    for s in sl:
        a = s[0]
        b = s[1]
        if a  in "HDCS" and b in "A23456789TJQK":
            continue
        else:
            break
    else:
        print("Yes")
        exit()
print("No")