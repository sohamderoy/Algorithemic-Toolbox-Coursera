no=int(input())
a=input()
b=a.split()
l=[]
m=[]
#print(b)
#print(type(b[0]))
for i in b:
    m.append(int(i))
#print(type(m[0]))
count=0
for i in range(len(m)):
    for j in range (i+1, len(m)):
        k=m[i]*m[j]
        count=count+1
        l.append(k)
#print(l,count)
l.sort()
print(l[-1])

