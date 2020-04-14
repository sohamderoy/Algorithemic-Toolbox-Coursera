import sys
import math
d=int(input())
m=int(input())
n=int(input())
s=list(map(int, input().split()))
#####################################################
#creating a helping list
s2=[0]
for _ in s:
    s2.append(_)
s2.append(d)
refill=0
#print(s2)
#####################################################
#some complicated stufffffffff
#for refrence look at the previous commit for this section
s1=s
s1.append(d)
s3=[0]
s3.append(s1[0])
for k in range (1,len(s1)):
    s3.append(s1[k]-s1[k-1])
#print(s2,2)
#s2.append(-1)
flag=False
for g in s3:
    if g>m:
        flag=True
        break
#print(flag,3)

######################################################
if m>d:
    print(0)
    sys.exit()
elif flag==True:
    print(-1)
    sys.exit()
else:
    start=0
    i=start+1
    while(i<=len(s2)-1):
        if (s2[i]-s2[start])<=m:
            try:
                i=i+1
            except:
                sys.exit()
        else:
            start=i-1
            refill=refill+1
    print(refill)
