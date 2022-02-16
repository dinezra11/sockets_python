"""
    Echo-Server example.

    Client side script.
    The general process of a server will be the following:
        declaration > connect >>> read/write >>> close
"""
import socket

server = ""
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # SOCK_STREAM -> TCP socket connection

try:
    print("Connecting to server..")
    s.connect((server, port))  # Attempt to connect to the server
    print("Connected to the server!")

    while True:
        data = input("Enter data to send to the server. Enter 'exit' to quit: ")
        if data == "exit":
            break

        print("Sending the message..")
        s.send(data.encode())
        print("Message back from the server: {}\n".format(s.recv(1024).decode()))

except socket.error as e:
    print(e)
finally:
    # User wants to stop. Close the socket and end the program.
    s.close()
    print("See you soon!")
