import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999

# connection to hostname on the port.
s.connect((host, port))
s.send('{"method":"sum", "x":2,"y":3}')
# Receive no more than 1024 bytes
tm = s.recv(1024)

s.close()

print("sum =  %s" % tm.decode('ascii'))