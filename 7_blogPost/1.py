l = [2,3,5,8,1,3]

a = 0
i=0
j=1

for k in range(2,len(l)):

    if l[k]>l[j]:
        
        if l[i] + l[j] == l[k]:
            a=a+1
        elif l[i]+l[j]!=l[k]:
            a=0
    else:
        p=1
        d=l[k]
        for m in range(k+1,len(l)):
            d= (d*(10**p))+l[m]
           
            if d>l[j]:
               break
            else:
                pass
        print(d)

                    
        k=k+p 
        if k==len(l)-1:
            break  
    i=j
    j=k
if l[i] + l[j] == l[k]:
    a=a+1
  
        




if a==0:
    print(False)
else:
    print(True)