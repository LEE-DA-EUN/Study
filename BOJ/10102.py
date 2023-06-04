v = int(input())
tp = list(input())
a = 0
b = 0
for i in range(v):
    if tp[i] == 'A':
        a = a + 1
    else:
        b = b + 1

if a > b:
    print("A")
elif b > a:
    print("B")
else:
    print("Tie")