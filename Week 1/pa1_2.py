no=int(input())
a=input()
b=a.split()
l=[]
m=[]
#print(b)
#print(type(b[0]))
for i in b:
    m.append(int(i))
m.sort()
print(m[-1]*m[-2])