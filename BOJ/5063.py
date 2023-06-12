t = int(input())
for i in range(t):
    r, e, c = map(int, input().split())
    ec = e-c
    if r > ec:
        print("do not advertise")
    elif r < ec:
        print("advertise")
    else:
        print("does not matter")
