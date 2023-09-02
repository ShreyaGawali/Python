lower=1
upper=25
print("Prime Numbers between {} and {} are".format(lower,upper))
for num in range(lower,upper+1):
        for i in range(2,num):
               if(num % i) == 0:
                  break
               else:
                 print(num)