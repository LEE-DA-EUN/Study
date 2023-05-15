t = int(input())
for i in range(1, t+1):
    n = int(input())
    a = 0
    for j in range(1, n+1):
        if j%2==1:
            a = a+j
        else:
            a = a-j
    print(f"#{i} {a}")