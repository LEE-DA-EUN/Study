t = int(input())
for i in range(1, t+1):
    a, b = map(int, input().split())
    print("#", end="")
    print(i, end=" ")
    print(a//b, end=" ")
    print(a%b)