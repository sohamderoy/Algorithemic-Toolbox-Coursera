#trial of assignment two by different method
n=int(input())
m=[int(x) for x in input().split()]
(large,seclarge)=(0,0)
for i in m:
    if i>large:
        large=i
k=m.count(large)
if k>1:
    print(large*large)
else:
    for i in m:
        if i!=large and i>seclarge:
            seclarge=i
    print(large*seclarge)