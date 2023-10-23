while(1):
    ls = list(map(int, input().split()))
    ls.sort()
    if ls[0] == 0:
        break

    if ls[2]**2 == ls[0]**2 + ls[1]**2:
        print('right')
    else:
        print('wrong')
