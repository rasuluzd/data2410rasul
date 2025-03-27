#import socket module
from socket import *
import sys  # Used to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)# Create a TCP socket

# Set server port number
serverPort = 8000
# Binds the server to listen on all available network interfaces on port 8000
serverSocket.bind(('', serverPort))
# Start listening for incoming connections, whereonly 1 connection can wait in queue
serverSocket.listen(1)
print('Ready to serve...')

while True:
    # Accept a new connection from a client
    connectionSocket, addr = serverSocket.accept()
    try:
        # Receive request from the client (max 1024 bytes)
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        # Opens the requested file
        f = open(filename[1:])
        # Reads the file contents
        outputdata = f.read()
        f.close()
        # Send HTTP response header
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        # Send the file contents to the client
        for i in range(len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        # Add a newline to mark the end of the response
        connectionSocket.send("\r\n".encode())
        # Close the connection
        connectionSocket.close()
    
    except IOError:
        # If the requested file doesn't exist, it will send a 404 response
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>\r\n".encode())

        # Close the connection after sending the error message
        connectionSocket.close()

# This part is technically unreachable due to the infinite loop, 
# but if the server were to stop, it would close the socket and exit
serverSocket.close()
sys.exit()
