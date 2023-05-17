t = int(input())
for i in range(1, t+1):
    a = list(input())
    a.reverse()
    for j in range(len(a)):
        if a[j] == 'b':
            a[j] = 'd'
        elif a[j] == 'd':
            a[j] = 'b'
        elif a[j] == 'p':
            a[j] = 'q'
        else:
            a[j] ='p'
    ans = ''.join(a)
    print(f"#{i} {ans}")