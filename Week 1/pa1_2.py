no=int(input())
m=[int(x) for x in input().split()]
m.sort()
print(m[-1]*m[-2])