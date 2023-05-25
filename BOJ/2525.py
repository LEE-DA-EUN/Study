a, b = map(int, input().split())
c = int(input())
ans2 = (b + c) % 60
bc = (b + c) // 60
ans1 = (a + bc) % 24
print(ans1, ans2)
