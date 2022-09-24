x, y, z = map(int, input().split())
if x > 0:
    if y > 0:
        if y > x:
            print(x)
        else:
            if z > 0:
                if z > y:
                    print(-1)
                else:
                    print(x)
            else:
                print(2 * abs(z) + x)
    else:
        print(x)
else:
    if y < 0:
        if y < x:
            print(-x)
        else:
            if z < 0:
                if z < y:
                    print(-1)
                else:
                    print(-x)
            else:
                print(2 * z - x)
    else:
        print(-x)
