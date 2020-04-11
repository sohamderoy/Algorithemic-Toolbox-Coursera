# Python 3 Program to find sum of  
# Fibonacci numbers using Pisano Period
#[ 0 | 1 | 1 | 2 | 3 | 5  | 8  | 13 | 21 | 34 | 55  | 89  | 144 | 233 ]<- f(n)
#[ 0 | 1 | 2 | 4 | 7 | 12 | 20 | 33 | 54 | 88 | 143 | 232 | 376 | 609 ]<-Addition values***
#[ 0 | 1 | 2 | 3 | 4 | 5  | 6  | 7  | 8  | 9  | 10  | 11  | 12  | 13  ]<- n
n=59 #pisano period for n=10 is 60 where n is as per the expresion F(x)%n
m=int(input())
m=(m%60)
(k,f,g)=([0],[0,1],[])
for i in range(n):
    f.append(f[i+1]+f[i])
#generating Pisano Period
for i in range(1,n+2):
    k.append(k[-1]+f[i]) #generating the Addition values***
for i in k:
    g.append(i%10) 
#print(m)
print(g[m])
