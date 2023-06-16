t = int(input())
for i in range(t):
    c = int(input())
    aa = ''
    ans = 0
    for j in range(c):
        a, b = input().split()
        b = int(b)
        if b > ans:
            ans = b
            aa = a
    print(aa)