for i in range(1, 11):
    n = input()
    find = list(input())
    test = list(input())
    ans = 0
    for j in range(len(test)-len(find)+1):
        if find[0] == test[j]:
            for k in range(len(find)):
                if find[k] != test[j+k]:
                    a = 0
                    break
                else:
                    a = 1
            ans = ans+a
    print(f"#{i} {ans}")