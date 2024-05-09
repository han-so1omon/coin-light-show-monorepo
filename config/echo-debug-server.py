import socket

def echo_server(host, port):
    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Bind the socket to the address and port
        s.bind((host, port))
        # Enable the server to accept connections (make it a listening socket)
        s.listen()
        print(f"Echo server is running on {host}:{port}")

        # Infinite loop to keep the server running
        while True:
            # Accept a connection
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    # Receive data from the client
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(f"Received data: {data}")
                    # Send the received data back to the client
                    conn.sendall(data)

if __name__ == '__main__':
    # Specify the IP address and port number
    # (use "localhost" or "127.0.0.1" for local testing)
    HOST = '0.0.0.0'
    PORT = 65432
    echo_server(HOST, PORT)