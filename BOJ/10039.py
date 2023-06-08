ans = 0
for i in range(5):
    a = int(input())
    if a < 40:
        a = 40
    ans = ans + a
print(ans//5)
