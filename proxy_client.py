import socket

BYTES_TO_READ = 4096


def connect():
    host = "127.0.0.1"
    port = 8080
    req = b"GET / HTTP/1.1\nHost: www.google.com\n\n"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.send(req)
        s.shutdown(socket.SHUT_WR)

        print("Waiting...")

        full_data = b""
        while True:
            data = s.recv(BYTES_TO_READ)
            if not data:
                break
            full_data += data
        print(full_data)

        s.close()


def main():
    connect()


if __name__ == "__main__":
    main()
