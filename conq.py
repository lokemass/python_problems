n=int(input("number of value"))
a=[]
v=[]
mod=[]
m=[]
y=[]
tou=1
x=0
for i in range(n):
    print("x",i)
    temp=int(input())
    v.append(temp)
    temp2=int(input())
    mod.append(temp2)
    print("x",i,"=",v[i],"(mod",mod[i],")")
    
for i in range(n):
    tou=tou*mod[i]
    
print("tou = ", tou)
for i in range(n):
    m.append(tou/mod[i])
print("M values are",m)
for i in range(n):
    y.append(m[i]%mod[i])
for i in range(n):
    print("the value of y",i,"=",y[i])
for i in range(n):
    x=x+(v[i]*m[i]*y[i])
print("the value of x= ",x)
print("the final value of x=",x%tou)
           
    
