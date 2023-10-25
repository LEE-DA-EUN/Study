t = int(input())
for i in range(t):
    ans = 0
    n = 1
    ls = []
    a, b = map(int, input().split())
    for i in range(b):
        n = n*a%10
        if n not in ls:
            ls.append(n)
        else:
            break
    
    ptn = (b%len(ls))-1
    if ptn >= 0:
        ans = ls[ptn]
    else:
        ans = ls[len(ls)-1]
    
    if ans == 0:
        print(10)
    else:
        print(ans)