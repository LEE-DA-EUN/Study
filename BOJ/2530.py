a, b, c = map(int, input().split())
d = int(input())
s = (c + d) % 60
cd = (c + d) // 60
m = (b + cd) % 60
mp = (b + cd) // 60
h = (a + mp) % 24
print(h, m, s)
