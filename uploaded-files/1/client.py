import socket

HEADER = 64
SERVER = "127.0.1.1"
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISC"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(message):
    message = message.encode(FORMAT)
    msg_len = len(message)
    send_length = str(msg_len).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

send("HEys")
send("PEnis")

send(DISCONNECT_MESSAGE)