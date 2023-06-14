t = int(input())
for i in range(t):
    ls = list(input())
    a = 0
    b = 0
    for j in ls:
        if j == 'O':
            a = a + 1
            b = b + a
        else:
            a = 0
    print(b)