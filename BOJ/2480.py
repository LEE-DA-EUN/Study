a, b, c = map(int, input().split())
if a == b:
    if b == c:
        print(10000+a*1000)
    else:
        print(1000+a*100)
else:
    if b == c:
        print(1000+b*100)
    elif a == c:
        print(1000+a*100)
    else:
        t = [a,b,c]
        ls = list(t)
        print(max(ls)*100)