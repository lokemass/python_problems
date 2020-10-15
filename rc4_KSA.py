s=[]
k=[]
i=int()
j=int()
n=int(input("Enter the number of value N="))
print("S value are \n")
for a in range(n):
    temp=int(input())
    s.append(temp)
print("K value are \n")
for a in range(n):
    temp=int(input())
    k.append(temp)
print("S=",s)
print("K=",k)
i=0
j=0
for i in range(n):
    print("---------------------")
    print("iteration-",i)
    print("---------------------")
    print("j=(j +s[i]+k[i])mod n")
    print("j=(",j," +s[",i,"]+k[",i,"])mod ",n)
    print("j=",j,"+",s[i],"+",k[i])
    j=(j +s[i]+k[i])
    j=j%n
    print("J=",j)
    print("swap s[i],s[j]")
    print("swap s[",i,"],s[",j,"]")
    temp1=s[i]
    s[i]=s[j]
    s[j]=temp1
    print (s)

    

    
    
