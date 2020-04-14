#To calculate the highest salary that can be made by rearranging the given no.
#The idea is if in a series of [X,Y,Z,A,B,C]
#If XY > YX then the list remain same for that instance 
#But if XY < YX then the list becomes [Y,X,Z,A,B,C]
n1=int(input())
n2=list(map(int, input().split()))
t=True
(oldstr, newstr)=(str(),str())
for i in n2:
    oldstr=oldstr+str(i)
while t==True:
    for i in range (n1-1):
        XY=int(str(n2[i])+str(n2[i+1]))
        YX=int(str(n2[i+1])+str(n2[i]))
        if XY < YX:
            (n2[i],n2[i+1])= (n2[i+1],n2[i]) #if XY > YX then no need to swap, list will remain same for this instance.
    newstr=""
    for i in n2:
        newstr=newstr+str(i)
    if oldstr!=newstr:
        oldstr=newstr
    elif oldstr==newstr:
        t=False
        break
print(int(newstr))