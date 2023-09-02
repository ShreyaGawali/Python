num=int(input("Enter any number:"))
sum = 0
temp = num
while temp>0:
    digit = temp%10
    sum+ = digit
    temp// = 10
if num==sum:
    print("{} is an armstrong number".format(num))
else:
    print("{} is not an armstrong number".format(num) )