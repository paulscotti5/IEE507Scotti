import socket
import threading

HEADER = 64
PORT = 19251
SERVER = '192.168.0.105'
#socket.gethostbyname(socket.gethostname())
#osip = os.popen('curl ifconfig.me').readline()
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
#####
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #make new socket, primir argumento la familia de socket que posemos escojer
#AF_INET que tipo de ip o que tipo de address----y el segundo argumento simplemente es estandar donde le decimo que queremos un socket
#para stream
server.bind(ADDR)#ADDR necesariemente necesita ser un tuple.
mac_cliente='90-2B-34-0C-A0-01'


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True



    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) #HEDEAR how many bytes we recive
        if msg_length: #if the message has some content
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            mac_recibida=msg
            if mac_recibida!=mac_cliente:
                conn.close()
                print("Conexión rechazada")
                conn.send("Conexión rechazada".encode(FORMAT))
            elif mac_recibida==mac_cliente:
                print("Conexión exitosa")
                conn.send("Conexión exitosa".encode(FORMAT))
                break
            else:
                print("Error de autenticación")
                conn.send("Error de autenticación".encode(FORMAT))
                conn.close()


    #cuando estemso conectados


    connected=True
            #separar datos
    while connected:

        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length: #if the message has some content
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))

    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on address {ADDR}")
    while True:
        conn, addr = server.accept()#espera aca hasta que ocurra una nueva conexión donde guarda el objeto socket y el address el cual nos permite
        #                               comunicaros hace el cliente
        #ahora declaramos un threath para manejar la conección de ese cliente
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        #imprimir cuantas conexiónes activas tenemos
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()




cursor.commit()
