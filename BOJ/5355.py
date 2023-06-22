t = int(input())
for i in range(t):
    ip = list(map(str, input().split()))
    ans = float(ip[0])
    for j in range(1, len(ip)):
        if ip[j] == '@':
            ans = ans * 3
        elif ip[j] == '%':
            ans = ans + 5
        elif ip[j] == '#':
            ans = ans - 7
    print("{:.2f}".format(ans))