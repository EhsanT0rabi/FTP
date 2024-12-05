import os
import socket
import threading

from Server.util import server_command

SERVER_START_PATH = os.path.abspath("../Public")


class Server:
    def __init__(self, port):
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.bind_socket()
        self.sock.listen(5)  # Allow up to 5 connections
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print(f"Server running on port {self.port}")

    def bind_socket(self):
        while True:
            try:
                self.sock.bind(("", self.port))
                break
            except OSError:
                self.port += 1

    def accept_connections(self):
        while True:
            try:
                conn, addr = self.sock.accept()
                threading.Thread(target=self.handle_connection, args=(conn, addr)).start()
            except KeyboardInterrupt:
                print("Server stopped.")
                self.shutdown()
                break
            except Exception as e:
                print(f"Error accepting connection: {e}")

    def handle_connection(self, conn: socket.socket, addr):
        print(f"[+] User connected: {addr}")
        with conn:
            while True:
                try:
                    data = conn.recv(4096)
                    if not data:
                        break
                    server_command.command_parser(data, conn, addr)
                except ConnectionResetError:
                    print(f"[-] Connection reset by {addr}")
                    break
                except Exception as e:
                    print(f"Error handling connection from {addr}: {e}")
                    break

    def shutdown(self):
        self.sock.close()


def main():
    server = Server(8021)
    server.start()
    server.accept_connections()


if __name__ == "__main__":
    main()
