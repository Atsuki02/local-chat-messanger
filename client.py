import socket
import sys

# create socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# set the path where the server is waiting
server_address = '/tmp/socket_file'
print('connecting to {}'.format(server_address))

# try to connect with the server
try:
    sock.connect(server_address)
except socket.error as err:
    print(err)

    sys.exit(1)

# get cli input from the user
try:
    print("Enter your message:")
    user_input = input()
    # convert input to binary data
    message = user_input.encode('utf-8')
    # send to the server
    sock.sendall(message)


    # set 2 seconds timeout
    sock.settimeout(2)

    # If there is a response from the server, display it
    try:
        while True:

            data = sock.recv(32)

            if data:
                # convert binary data to string data
                servre_response = data.decode('utf-8')
                # display the response
                print('Server response: ' + servre_response)

            else:
                break
    except(TimeoutError):
        print('Socket timeout, ending listening for server messages')

# close the socket 
finally:
    print('closing socket')
    sock.close()