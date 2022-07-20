k1, b1 = map(int, input().split())
k2, b2 = map(int, input().split())
if k1 == k2:
    if b1 == b2:
        print('coincide')
    else:
        print('parallel')
else:
    x = -(b1 - b2) / (k1 - k2)
    y = k1 * x + b1
    print('intersect')
    print(type(x))
    print(isinstance(x,float))
    print(int(x), int(y))
