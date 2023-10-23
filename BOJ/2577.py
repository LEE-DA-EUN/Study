a = int(input())
b = int(input())
c = int(input())

num = a*b*c
ans = list(str(num))
for i in range(10):
    print(ans.count(str(i)))
