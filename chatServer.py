import socket
s=socket.socket()
s.bind(("localhost",4444))
s.listen(1)
print("SSP is ready to accept any CSP:")
print("="*40)
while(True):
    cs,addr=s.accept()
    csdata=cs.recv(1024).decode()
    print("Student Msg---->{}".format(csdata))
    sdata=input("DSoft---->")
    cs.send(sdata.encode())