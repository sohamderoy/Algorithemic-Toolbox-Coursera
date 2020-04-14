#To find the minimum no of refueling that need to be done to reach from point A to B
import sys
import math
d=int(input())
m=int(input())
n=int(input())
s=list(map(int, input().split()))
count=0
s1=s
s1.append(d)
#print(s1,1)
s3=[0]
s3.append(s1[0])
for i in range (1,len(s1)):
    s3.append(s1[i]-s1[i-1])
#print(s2,2)
#s2.append(-1)
flag=False
for i in s3:
    if i>m:
        flag=True
        break
#print(flag,3)
refill=0
if m>d:
    print(0)
    sys.exit()
elif flag==True:
    print(-1)
    sys.exit()
elif flag==False and m<d:
    start=0
    i=start+2
    while(i<=len(s2)):
        if (sum(s2[start+1:i])<m):
            i+=1
            if (s2[i]==-1):
                break
        elif (sum(s2[start+1:i])>m):
            start=i-2
            refill=refill+1
            if s2[i]==-1:
                break
print(refill+)
    
