t = int(input())
for i in range(1, t+1):
    a, b, c, d = map(int, input().split())
    m = (b+d)%60
    mh = (b+d)//60
    h = a+c+mh
    if h==12 or h==24:
        ansh = 12
    else:
        ansh = h%12
    print(f"#{i} {ansh} {m}")