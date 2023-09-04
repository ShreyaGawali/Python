def sumop(a,b):
    c=a+b
    return c

#anonymous object

addop=lambda a,b:a+b

#main function

print("type of sumop=",type(sumop))
res=sumop(10,10)
print("sum using normal function is {}".format(res))
print("type of addop=",type(addop))
res1=addop(1,2)
print("sum using anonymous function is {}".format(res1))
