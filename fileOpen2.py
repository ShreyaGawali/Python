# we are just opening the file using with open statement

with open("addr2.data","w") as fp:
    print("mode of file:",type(fp))
    print("is file readable:",fp.readable())
    print("is file writable:", fp.writable())
    print("is file closed:", fp.closed)

print("after leaving with open block ")
print("is file closed:", fp.closed)
