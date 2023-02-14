#!/usr/bin/python3

import json
import socket
import random
import time



# Set up the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("0.0.0.0", 8081))
server_socket.listen(1)

delay = 0.1
ramp_factor = 1 / 1.01
# Wait for a client to connect

while True:
    client_socket, client_address = server_socket.accept()
    print("Client connected from", client_address)

    for i in range(1000000):
        obj = {'a': int(i + 234), 'b': int(i), 'c': int(i // 2),
                'd': int(i // 3), 'e': int(i)}
        client_socket.sendall(json.dumps(obj).encode() + b'|')
        # time.sleep(delay)
        # delay *= ramp_factor

    print("Done")

    # Close the client and server sockets
    client_socket.close()
    
server_socket.close()
