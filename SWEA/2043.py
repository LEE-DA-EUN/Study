P, K = map(int, input().split())
a = 0
if P>=0 and P<=999:
    for i in range(K, P+1):
        a = a+1
    print(a)

    #k가 p보다 크면 멈추게 해야할 필요도 있는 거 같다