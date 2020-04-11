#gcd of two no using the Key Lemma concept
#Key Lemma concept says that gcd(a,b) = gcd(a',b) = gcd(b,a') where a' = a%b
n=[int(x) for x in input().split()]
if (n[1]>n[0]):
    (n[0],n[1])=(n[1],n[0]) #swapping values of n1 and n2 to make n1>n2
while (n[1]!=0):
    n[0]=n[0]%n[1]
    (n[0],n[1])=(n[1],n[0])
    if n[1]==0:
        print(n[0])
        break

