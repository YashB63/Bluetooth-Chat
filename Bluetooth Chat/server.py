import socket
server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server.bind(("Enter the mac address of your bluetooth(YOu will find it in device manager)", 4))
server.listen(1)

client, addr = server.accept()

try:
    while True:
        data = client.recv(1024)
        if not data:
            break
        print(f"Message: {data.decode('utf-8')}")
        message = input("Enter Message: ")
        client.send(message.encode("utf-8"))
except OSError as e:
    pass

client.close()
server.close()