"""
    Echo-Server example.

    Server side script.
    The general process of a server will be the following:
        declaration > bind > listen > accept >>> read/write >>> close
"""
import socket

server = ""
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # SOCK_STREAM -> TCP socket connection

try:
    # Initialize the server and bind the socket to the address and port
    s.bind((server, port))
    s.listen(2)
    print("Waiting for a connection, server started.")

    # Accept connection from the client
    conn, addr = s.accept() # accept() will wait until a connection is made.
    print("Connected to: {}".format(addr))

    while True:
        print("Waiting for data from the client...")
        data = conn.recv(1024) # Receive data from the client
        print("Data from client: {}".format(data.decode()))
        conn.send(data) # Send the data back to the client (echo-server)

except socket.error as e:
    print(e)
except BaseException as e:
    print(e)
finally:
    s.close()




