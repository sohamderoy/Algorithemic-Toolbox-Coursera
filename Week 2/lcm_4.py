#Finding the LCM of two no using the concep that LCM * GCD = a*b and Key Lemma concept to compute the GCD
#Key Lemma concept says that gcd(a,b) = gcd(a',b) = gcd(b,a') where a' = a % b
n=[int(x) for x in input().split()]
(a,b)=(n[0],n[1])
#evaluating gcd using the Key Lemma concept
if (n[1]>n[0]):
    (n[0],n[1])=(n[1],n[0]) #swapping values of n1 and n2 to make n1>n2
while (n[1]!=0):
    n[0]=n[0]%n[1]
    (n[0],n[1])=(n[1],n[0])
    if n[1]==0:
        gcd=n[0]
        break
#evaluating LCM by LCM * GCD = a*b
print(int((a*b)/gcd))
