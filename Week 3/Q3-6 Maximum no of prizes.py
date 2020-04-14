#program to find the maximum way to distribute prizes (efficient process)
import sys
n=int(input())
w=[]
l=1
while (n>0):
    if (n<=2*l):
        w.append(n)
        n-=n
    else:
        w.append(l)
        n-=l
    l+=1
print(len(w))
for _ in w:
    print(_, end=' ')
