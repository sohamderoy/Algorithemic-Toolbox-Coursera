n=int(input())
sum=1
f=[0,1]
for i in range(n):
    f.append(f[i+1]+f[i])
print(f[n])