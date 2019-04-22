from socket import *

serverHost = 'localhost'
serverPost = 50007

rInput = raw_input('Digite algo para o servidor: ')

mensagem = []

mensagem.append( rInput )

sockobj = socket(AF_INET, SOCK_STREAM)

sockobj.connect((serverHost, serverPost))

for linha in mensagem:
    sockobj.send(linha)
    data = sockobj.recv(1024)
    print('Cliente recebeu:', data)
    sockobj.close()
