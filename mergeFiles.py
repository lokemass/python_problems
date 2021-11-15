def mergeFiles(a):
    a.sort()
    print(a)
    temp=0
    b=[]
    for i in range(0,len(a)-1,1):
        if not(a[1]):
            break
        else:
            temp=a[0]+a[1]
            a.remove(a[1])
        a[0]=temp
        b.append(temp)
        a.sort()
#         print(a)
    total=0;
    for i in b:
        total+=i
    return total

mergeFiles([4,8,6,12])
