# FTP Server and Client

## Overview

This project implements a simple FTP (File Transfer Protocol) server and client, allowing users to upload, download, and
manage files on a remote server. The server handles multiple user connections and provides various commands for file
management.

## Features

- User authentication with login functionality.
- File upload and download capabilities.
- Directory management (create, remove, change directories).
- File management (rename, remove files).
- List and display directory contents.
- Support for multiple concurrent users.

## Technologies Used

- Python
- Socket Programming
- Object-Oriented Programming
- File System Operations

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/EhsanT0rabi/FTP
   cd FTP
   ```

2. Install any required dependencies (if applicable):
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure that Python is installed on your system (Python 3.x is recommended).

## Usage

### Starting the Server

1. Navigate to the server directory.
2. Run the server script:
   ```bash
   python server.py <port>
   ```
3. The server will start and listen for incoming connections.

- port is optional(Default=8021)

### Connecting with the Client

1. Navigate to the client directory.
2. Run the client script:
   ```bash
   python client.py <port>
   ```

- port is optional(Default=8021)

### Available Commands

    1. login                                     - Authenticate with the FTP server.
    2. upload <filename>   <dest/path/on/server> - Upload a file to the server.
    3. download <filename> <dest/path/on/local>  - Download a file from the server.
    4. mkdir <dir_name>                          - Create a new directory on the server.
    5. rmdir <option=-r> <dir_name>              - Remove a directory from the server.You can use the "-r"
                                                   for remove none empty directory.
    6. rm <filename>                             - Delete a file from the server.
    7. cd <dir_name>                             - Change the current working directory(On server).
    8. lcd <dir_name>                            - Change the current working directory(On local).
    9. pwd                                       - Path of the current directory(On server).
    10. lpwd                                     - Path of the current directory(On local).
    11. resume                                   - Resume a previously interrupted file transfer (not implemented).
    12. rename <old_name> <new_name>             - Rename a file on the server.
    13. list or ls <path>                        - List files in the path on the server.(default: current directory on server).
    14. llist or lls <path>                      - List files in the path on local .(default: current directory on local).
    15. help or ?                                - Show short help message.
    16. help full                                - Show this help message.
    17. quit or exit                             - Close the connection and exit the client.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please create a pull request or open an issue.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

- [Python Documentation](https://docs.python.org/3/)
- [Socket Programming in Python](https://realpython.com/python-sockets/)
