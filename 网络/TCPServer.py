from  socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(1)

print('The server is ready to receive')
connectionSocket, addr = serverSocket.accept()
connectionSocket.send('123456')
sentence = connectionSocket.recv(1024)
capitalizedSentence = sentence.upper()
print(capitalizedSentence)
connectionSocket.send(capitalizedSentence)
connectionSocket.close()

