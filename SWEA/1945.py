t = int(input())
for i in range(1, t+1):
    x = int(input())
    a = 0
    while x%2 == 0:
        a = a + 1
        x = x/2
    b =0
    while x%3 == 0:
        b = b + 1
        x = x/3
    c =0
    while x%5 == 0:
        c = c + 1
        x = x/5
    d =0
    while x%7 == 0:
        d = d + 1
        x = x/7
    e =0
    while x%11 == 0:
        e = e + 1
        x = x/11
    print("#{} {} {} {} {} {}".format(i,a,b,c,d,e))