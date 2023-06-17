t = int(input())
for i in range(t):
    yw = 0
    kw = 0
    for j in range(9):
        y, k = map(int, input().split())
        yw = yw + y
        kw = kw + k
    if yw > kw:
        print('Yonsei')
    elif kw > yw:
        print('Korea')
    else:
        print('Draw')