def Primepark(a):
    ans=[]
    for upper in a:
        lower=int(1)
        count = 0
#         print("prime numbers between", lower,"and", upper, "are:")
        for num in range (lower, upper+1):
         if num>1:
          for i in range (2,num):
           if num % i==0:
            break
          else: 
        #     print(num)
            count += 1
        ans.append(count)
#         print ( "count_prime:", count )
    return ans;
Primepark([5,24,10])
