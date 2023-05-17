t = int(input())
for i in range(1, t+1):
    l,u,x = map(int, input().split())
    if x < l:
        ans = l-x
    elif x > u:
        ans = -1
    else:
        ans = 0
    print(f"#{i} {ans}")