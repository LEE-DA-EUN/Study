t = int(input())
q = d = ni = p = 0
for i in range(t):
    n = int(input())
    q = n//25
    n = n%25
    d = n//10
    n = n%10
    ni = n//5
    p = n%5
    print(q,d,ni,p)


