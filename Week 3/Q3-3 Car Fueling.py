#To find the minimum no of refueling that need to be done to reach from point A to B
import sys
import math
d=int(input())
m=int(input())
n=int(input())
s=list(map(int, input().split()))
start=-1
sum=0
count=0
s1=s
s1.append(d)
#print(s1)
s2=[]
s2.append(s1[0])
for i in range (1,len(s1)):
    s2.append(s1[i]-s1[i-1])
#print(s2)
flag=False
for i in s2:
    if i>m:
        flag=True
        break
if m>d:
    print(0)
    sys.exit()
elif flag==True:
    print(-1)
    sys.exit()
else:
    while (d>0):
        for i in range (start, n):
            if s[i+1]-start>m:
                start=i
                count=count+1
                d=d-s[i]
                break
print(count-1)