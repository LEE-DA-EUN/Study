k, n, m = map(int, input().split())
pay = k*n
if pay > m:
    print(pay-m)
else:
    print(0)