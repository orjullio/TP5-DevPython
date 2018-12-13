import socket

HOST = socket.gethostname()
PORT = 5000
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)
print('Esperado conexão na porta {}...'.format(PORT))
(msg, cliente) = udp.recvform(1024)
print(cliente, msg.decode('ascii'))
udp.close()

input('Pressione qq tecla pra sair...')