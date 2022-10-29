import socket
import uuid

HEADER = 64
PORT = 19251
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = '192.168.0.105'
#SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def get_mac():
  mac_num = hex(uuid.getnode()).replace('0x', '').upper()
  mac = '-'.join(mac_num[i: i + 2] for i in range(0, 11, 2))
  return mac


def send(msg):
    message = msg.encode(FORMAT) #encode the message in byte format o encode str in byte object
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)#encode the lenght of the message
    send_length += b' ' * (HEADER - len(send_length))# darle el largo al mensaje de 64
    #b'' byte representación
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


mac_cliente=get_mac()
print(mac_cliente)
send(mac_cliente)
input("Presione enter para continuar...")

Casos_activos = 123
muertes = 123
msg = "Casos_activos," + str(Casos_activos)+ ", muertes," + str(123)
send(msg)

test_data = list()
test_data = [12, 12]
data_socket = 'temperature='+str(test_data[0])+','+'Humidity='+str(test_data[1])
send(data_socket)
input()
send("Hello Everyone!")
input()
send("Hello EIE!")
print("El cliente ha iniciado una conversación...")
send("El cliente ha iniciado una conversación...")

while True:
    msgchat=input('Cliente: ')
    msgchat="Cliente: "+msgchat
    send(msgchat)

send(DISCONNECT_MESSAGE)


