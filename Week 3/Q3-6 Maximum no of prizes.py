#program to find the maximum way to distribute prizes (efficient process)
import sys
n=int(input())
w=[]
k=n
l=1
while (k>0):
    if (k<=2*l):
        w.append(k)
        k-=k
    else:
        w.append(l)
        k-=l
    l+=1
print(len(w))
for _ in w:
    print(_, end=' ')
