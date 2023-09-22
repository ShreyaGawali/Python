import socket,sys
while(True):
    s=socket.socket()
    s.connect(("localhost",4444))
    csdata=input("Student---->")
    if(csdata.lower()=="bye"):
        s.send("Bye DSoft,I have some work!".encode())
        sys.exit()
    else:
        s.send(csdata.encode())
        ssdata=s.recv(1024).decode()
        print("D'Soft---->{}".format(ssdata))
