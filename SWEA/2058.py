n = int(input())
b = 0
if n>=1 and n<=9999:
    list = list(map(int, str(n)))
    for i in range(0, len(list)):
        b = b + list[i]
    print(b)