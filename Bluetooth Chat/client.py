import socket
client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
client.connect(("Enter the mac address of your bluetooth(YOu will find it in device manager", 4))

try:
    while True:
        message = input("Enter Message: ")
        client.send(message.encode("utf-8"))
        data = client.recv(1024)
        if not data:
            break
        print(f"Message: {data.decode('utf-8')}")
except OSError as e:
    pass

client.close()
