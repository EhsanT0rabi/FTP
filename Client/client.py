import os
import socket as s
import sys

# Add the parent directory to the system path for module imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Client.util.client_command import FTPClient


def start_cycle(usr_socket):
    """Continuously prompt the user for input and process commands."""
    while True:
        try:
            FTPClient(usr_socket).cmdloop(intro="[+] You are connected.\nUse 'help' to see commands.")
        except TimeoutError:
            print("Timeout Error: Check your connection.")
        except Exception as e:
            print(f"An error occurred: {e}")


def connect_to_server(port):
    """Establish a connection to the FTP server."""
    try:
        with s.socket(s.AF_INET, s.SOCK_STREAM) as soc:
            soc.connect(('', int(port)))
            start_cycle(soc)
    except ValueError:
        print("Invalid port number. Please enter a valid integer.")
    except ConnectionRefusedError:
        print("Connection refused. Please check the server address and port.")
    except Exception as e:
        print(f"An error occurred while connecting: {e}")


def main():
    port = input("Enter Port: ")
    connect_to_server(port)


if __name__ == "__main__":
    main()
