n = int(input("enter number of names you want to add: "))
if(n<0):
    print("invalid data")
else:
    lst=[]
    for i in range(1,n+1):
        val=input()
        lst.append(val)
    else:
        print(lst)
        print("="*50)
        print("THE ORIGINAL NAMES ARE: ")
        for u in lst:
            print(u,end="\n")
        else:
            print("="*50)
            print("THE NAMES IN ASCENDING ORDER: ")
            val2=lst.sort()
            for val2 in lst:
                print(val2)
            else:
                print("="*50)
                print("THE NAMES IN DESENDING ORDER: ")
                val3=lst.sort(reverse=True)
                for val3 in lst:
                    print(val3)
print()
print("HAPPY HAPPY")



