# here we are just open the file using open
# and checking some conditions

fp=open("add1","w")
print("Type of file {}".format(type(fp)))
print("Mode of file:", fp.mode)
print("is file readable:",fp.readable())
print("is file writable:", fp.writable())
print("is file closed:", fp.closed)
fp.close()
print("after closing..is file closed:" , fp.closed)


