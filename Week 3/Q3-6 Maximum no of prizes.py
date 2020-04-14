#program to find the maximum way to distribute prizes
import sys
n=int(input())
(rem, l)=(int(), [0])
flag=True
i=1
while rem!=0 or flag==True:
    l.append(i)
    rem=n-i
    n=n-i
    i=i+1
    if rem in l:
        l[-1]=l[-1]+rem
        flag=False
        break
    #print(l)
l.pop(0)
print(len(l))
for _ in range (len(l)):
    print(l[_], end=' ')

