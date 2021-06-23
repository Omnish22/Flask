inp=input()
l = [int(l) for l in inp]

nl= []
i = 0 
j = 1 
c = 0 

nl.append(l[i])
for k in range(len(l)-1):
    if l[j]>l[i]:
        nl.append(l[j])
        i=j
        j=j+1
        if j>=len(l):
            break

    else:
        p=0
        value = l[j]
        for m in range(j+1,len(l)):
            p = p+1
            value = value*(10)+l[m]
            if value>l[i]:
                break
            else:
                pass

        nl.append(value)
        del l[0]
        l.insert(j+1,value)
        i=j+1
        j=j+p+1
        if j>=len(l):
            break
        
print(l)
print(nl)

ans=0
i=0
j=1
for k in range(2,len(nl)):
    if nl[i]+nl[j]==nl[k]:
        ans=ans+1
        i=j
        j=k
    else:
        ans=0
        break

if ans==0:
    print(False)
else:
    print(True)