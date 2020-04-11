def lastdigitofsum(m):
    n=59 #pisano period for n=10 is 60 where n is as per the expresion F(x)%n
    (k,f,g)=([0],[0,1],[])
    for i in range(n):
        f.append(f[i+1]+f[i])
#generating Pisano Period
    for i in range(1,n+2):
        k.append(k[-1]+f[i]) #generating the Addition values***
    for i in k:
        g.append(i%10) 
    return(g[m])
    print("g(m): ", g(m))
    print("my name is")

m=list(map(int, input().split()))
a=m[0]%60
b=m[1]%60
p=lastdigitofsum(a)
q=lastdigitofsum(b)
e={-1:9, -2:8, -3:7, -4:6, -5:5, -6:4, -7:3, -8:2, -9:1}
if q-p>0:
    print(q-p)
else:
    print(e[q-p])
