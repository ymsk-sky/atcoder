s = input()
if s[0] == "0":
    l = [[s[6]], [s[3]], [s[1], s[7]], [s[0], s[4]], [s[2], s[8]], [s[5]], [s[9]]]
    l2 = [False] * 7
    for i, r in enumerate(l):
        for p in r:
            if p == "1":
                l2[i] = True
    
    f1, f2, f3 = False, False, False
    for b in l2:
        if (not f1) and (not f2) and (not f3) and b:
            f1 = True
        
        if f1 and (not f2) and (not f3) and (not b):
            f2 = True
        
        if f1 and f2 and (not f3) and b:
            f3 = True
    if f1 and f2 and f3:
        print("Yes")
    else:
        print("No")

else:
    print("No")
