#filter function ek special function hai.vo values ko filter karke deta hai.jaise yaha par even and odd values ko filter kiya
#filter function me 2 parameter bhejne padte. pahila parameter function ka naam rahta aur dusra parameter
#list rahti......list ke ek ek element function me jata hai aur filter hota hai......

def even(n):
    if n%2==0:
        return True
    else:
        return False

def odd(n):
    if n%2!=0:
        return True
    else:
        return False

#main program
lst=[11,23,14,15,12,66,44,77,86,78,98,90,65,35]
obj1=filter(even,lst)
evenobj=list(obj1)
print("given list is {}".format(lst))
print("even element from the list are {}".format(evenobj))
obj2=filter(odd,lst)
oddobj=list(obj2)
print("odd element from the list are {}".format(oddobj))