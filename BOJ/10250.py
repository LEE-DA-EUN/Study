t = int(input())
x = y  = 0
for i in range(t):
    h,w,n = map(int, input().split())
    y = (n%h) * 100
    x = n//h + 1
    if y == 0:
        y = h * 100
        x -= 1
    print(x+y)