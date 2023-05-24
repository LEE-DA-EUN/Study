a = int(input())
b = input()
c = int(b)
d = list(b)
for i in range(2,-1,-1):
    print(a*int(d[i]))
print(a*c)