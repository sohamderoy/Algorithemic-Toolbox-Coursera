# to find ou thte last no of a fibonachi series
n=int(input())
sum=1
f=[0,1,0]
for i in range(n):
    f[2]=(f[1]+f[0])
    f[0]=f[1]
    f[1]=f[2]
print(f[0])