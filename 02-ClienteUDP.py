import socket

HOST = socket.gethostname()
PORT = 5000
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
msg = input('Entre com a mensagem:\n')
udp.sendto(msg.encode('ascii'), dest)
udp.close()