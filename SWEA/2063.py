n = int(input())
if n>= 9 and n<=199:
    list = list(map(int, input().split()))
    list.sort()
    a = n//2
    print(list[a])