t = int(input())
for i in range(1, t+1):
    a = input()
    ls = ['SAT','FRI','THU','WED','TUE','MON','SUN']
    if a in ls:
        print(f"#{i} {ls.index(a)+1}")