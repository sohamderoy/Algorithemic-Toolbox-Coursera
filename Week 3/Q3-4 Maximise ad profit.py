n=int(input())
a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
a.sort()
b.sort()
c=[]
for i in range(len(a)):
    c.append(a[i]*b[i])
print(sum(c))
