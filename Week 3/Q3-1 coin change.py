# to find the minimum number of coins with denominations 1, 5, 10 that changes 𝑚.
n=int(input())
if n in range (0,5):
    print(n)
elif n in range (5,10):
    k=n-5
    print(k+1)
elif n>10:
    (k,r)=(int(n/10), int(n%10))
    if r in range (0,5):
        print(r+k)
    elif r in range (5,10):
        r2=r-5
        print(k+1+r2)
