t = int(input())
for i in range(1, t+1):
    a, b = map(int, input().split())
    if a>=0 and a<=10000:
        if b>=0 and b<=10000:
            print(f"#{i}", end=" ")
            if a>b:
                print(">")
            if a==b:
                print("=")
            if a<b:
                print("<")