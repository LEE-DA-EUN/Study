t = int(input())
for i in range(1, t+1):
    n, m = map(int, input().split())
    nls = list(map(int, input().split()))
    mls = list(map(int, input().split()))
    if len(nls)<len(mls):
        a = nls
        b = mls
    else:
        a = mls
        b = nls		#짧은 길이 a, 긴 길이 b로 치환함
    lst = list()
    for x in range(0, len(b)-len(a)+1):
        case = 0
        for y in range(0, len(a)):
            xx = a[y]*b[y+x]
            case = case + xx
        lst.append(case)
        ans = max(lst)
    print(f"#{i} {ans}")