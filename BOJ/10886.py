t = int(input())
c = 0
nc = 0
for i in range(t):
    num = int(input())
    if num == 1:
      c = c + 1
    else:
        nc = nc + 1
if c > nc:
    print("Junhee is cute!")
else:
    print( "Junhee is not cute!")