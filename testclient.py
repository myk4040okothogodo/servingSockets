import ssl
import socket
from envar import *

hostname = LOCALHOST_NAME

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations('/home/mykmyk/serva/sava2/keys/Demo.pem')

with socket.socket(socket.AF_INET, socket.SOCKET_STREAM) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        print(ssock.version())
