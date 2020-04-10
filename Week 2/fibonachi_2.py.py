#to find the last digit of the last no of a fibonachi series [fast version] 
#reduces time form 9.98/5.00 -> 0.26/5.00 (approx machine values)
n=int(input())
sum=1
f=[0,1,0]
for i in range(n):
    f[2]=(f[1]+f[0])
    f[0]=f[1]%10 #we only need the last digit of every no., so that cuts the computation time
    f[1]=f[2]%10 #we only need the last digit of every no., so that cuts the computation time
print(f[0]%10)