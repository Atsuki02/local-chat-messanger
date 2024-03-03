import socket
import os
from faker import Faker

# create socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# set the path where the server is waiting for connection
server_address = '/tmp/socket_file'

# create the instance of Faker class
fake = Faker()

# delete the connection in case last connection still remains
try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print('Starting up on {}'.format(server_address))

# bind socket to the server address
sock.bind(server_address)

# ask and wait for the connection 
sock.listen(1)

# start the loop 
while True:
    # accept the connection from the client
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)


        while True:
            # receive data from the server
            data = connection.recv(16)
            # convert data to str data
            data_str = data.decode('utf-8')

            print('Received ' + data_str)

            if data:
                # generate a random name
                response = fake.name()

                # respond back to the client
                connection.sendall(response.encode())

                # if no data from the client, end the loop
            else:
                print('no data from', client_address)
                break
    # close connetion
    finally:
        print("Closing current connection")
        connection.close()