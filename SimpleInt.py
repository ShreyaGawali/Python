p = int(input("Enter the principal amount:"))
t = int(input("Enter the period:"))
i = int(input("Enter the rate of interest:"))
simpleint = (p*t*i)/100
totalamo = p+simpleint
print("------------------------------------------------")
print("\tprincipal amount={}".format(p))
print("\ttime period is {}".format(t))
print("\trate of interest is {}".format(i))
print("\tsimple interest is {}".format(simpleint))
print("\ttotal amount is {}".format(totalamo))




