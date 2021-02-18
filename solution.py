 #import socket module
from socket import *
import sys #In order to terminate the program

def webServer(port=13331):
   serverSocket = socket(AF_INET, SOCK_STREAM)
   serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) #reset server socket

   #Fill in start
   serverSocket.bind(('',port)) #Prepare a server socket
   serverSocket.listen(1)
   #Fill in end

   while True:
       #Fill in start
       print('Ready to serve...')
       connectionSocket, addr = serverSocket.accept() #Establish the connection
       #Fill in end


       try: #Fill in start
           message = connectionSocket.recv(1024) .decode()
           print(message, message.split()[0], message.split()[1])
           filename = message.split()[1]
           f = open(filename[1:])
           outputdata = f.read()
           print(outputdata)
           connectionSocket.send('\nHTTP/1.1 200 OK\n\n') #Send one HTTP header line into socket
           connectionSocket.send(outputdata) #Send the content of the requested file to the client
           #Fill in end

for i in range(0, len(outputdata)):
           connectionSocket.send(outputdata[i].encode())

           connectionSocket.send("\r\n".encode())
           connectionSocket.close()
       except IOError: #Fill in start
           connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n')  #Send response message for file not found (404)
           connectionSocket.close() #Close client socket
           #Fill in end

   serverSocket.close()
   sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
   webServer(13331)
