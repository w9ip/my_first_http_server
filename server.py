import socket

server = socket.create_server(("127.0.0.1", 8000, )) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.listen(10)

try:
    while True:
        client_socket, address = server.accept()

        recieved_data = client_socket.recv(1024).decode("utf-8")
        
        print("Получили данные от клиента", recieved_data)

        path = recieved_data.split()[1]

        response = f"HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8\n\n" \
            f"Hello, World!<br />Path: {path}"
        
        client_socket.send(response.encode("utf-8"))
        client_socket.close()
except KeyboardInterrupt:
    server.close()