#to find f(n) mod m using Pisano Period
'''
#finding the pattern in a list
k=[0,1,1,2,0,2,2,1,0,1,1,2,0,2,2,1,0,1,1,2,0,2,2,1,0,1,1,2,0,2,2,1]
j=0
for i in range(2,len(k)):
    if (k[j:i])==(k[i:i+len(k[j:i])]): #slicing 2 adjacent part of the list to check if they are equal or not
        break                          #if equal then pattern is found with the period being the length of the final slice
print(i)
#i=8
#print(k[j:i])
#print(k[i:i+len(k[j:i])])
'''
maxf=10000
n=[int(x) for x in input().split()]
(k,f,g)=([0],[0,1],[])
for i in range(maxf):
    f.append(f[i+1]+f[i])
for i in f:
    g.append(i%n[1])
#print(g)
j=0
for i in range(2,len(g)):
    if (g[j:i])==(g[i:i+len(g[j:i])]):
        break
#print(i)
m=n[0]%i
print(g[m])
