import socket
import time
import json
# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999

def sum(json):
    x= json["x"]
    y = json["y"]

    return x+y

func_map = {
    "sum" : sum
}

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()

    print("Got a connection from %s" % str(addr))
    currentTime = time.ctime(time.time()) + "\r\n"
    json_data = json.loads(clientsocket.recv(1024))
    print(json_data)
    res = func_map[json_data["method"]](json_data)
    print (res)
    clientsocket.send(json.dumps(res))

    clientsocket.close()