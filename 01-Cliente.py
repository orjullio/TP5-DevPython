# Máquina Cliente

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Tenta se conectar ao servidor
    s.connect(('10.0.2.15', 9999))
    msg = 'Olá, servidor!\n'
    # Envia uma mensagem codificada em bytes ao servidor
    s.send(msg.encode('ascii'))
    # Fecha conexão com o servidor
    s.close()
except Exception as erro:
    print(str(erro))