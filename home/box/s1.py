import socket

HOST = '0.0.0.0'                 # Symbolic name meaning all available interfaces
PORT = 2222              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            if not data: break
            if data == 'close': break
            conn.sendall(data)
