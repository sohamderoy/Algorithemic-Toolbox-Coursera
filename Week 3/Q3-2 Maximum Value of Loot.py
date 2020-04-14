# Output the maximal value of fractions of items that fit into the knapsack
n=[int(x) for x in input().split()]
total=n[1]
value=0.0000
(v,w,vperw)=([],[],[])
for i in range(n[0]):
    k=list(map(int, input().split()))
    v.append(k[0])
    w.append(k[1])
    k.clear()
#print(v,w)
for i in range(n[0]):
    vperw.append(v[i]/w[i])
#print(vperw)
if (n[1]!=0):
    while(n[1]!=0 and n[1]>0 and len(vperw)!=0):
        m=max(vperw)
        pos=vperw.index(m)
        if w[pos]<=n[1]:
            n[1]=n[1]-w[pos]
            value=float(value+v[pos])
            v.pop(pos)
            w.pop(pos)
            vperw.pop(pos)
        elif w[pos]>n[1]:
            #print(v,w,vperw,m,pos)
            frac=float(n[1]/w[pos])
            n[1]=n[1]-w[pos] #this line should make n[1] negative, i.e. there is no more space in the bag and the loop will end
            #print(frac)
            value=float(value+frac*v[pos])
            break
    print('%0.4f'%value)        
elif (n[1]==0):
    print(0.0000)
