from itertools import permutations

n = int(input())
num = list(permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9'], 3))

for _ in range(n):
    check, s, b = map(int, input().split())
    check = list(str(check))
    rm = 0

    for i in range(len(num)):
        sn = bn = 0
        i -= rm

        for j in range(3):
            if num[i][j] == check[j]:
                sn += 1
            elif check[j] in num[i]:
                bn += 1
        
        if sn != s or bn != b:
            num.remove(num[i])
            rm = rm + 1
    
print(len(num))     
