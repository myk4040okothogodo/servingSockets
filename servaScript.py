import socket
import ssl
from router import router
import ssl
from envar import *
import os
import signal
import errno
from clientReq import request
from url_rewrite import *

def grim_reaper(signum, frame):
    while True:
        try:
            pid, status = os.waitpid(
                -1,          # Wait for any child process
                 os.WNOHANG  # Do not block and return EWOULDBLOCK error
            )
        except OSError:
            return

        if pid == 0:  # no more zombies
            return

def handle_request(connection):
    requeststr = connection.recv(1024).decode('utf-8')
    requestObject = request(requeststr)
    print(request)
    handleThisRequest = router(rewrite_url(requestObject))
    connection.send(handleThisRequest.routing())
                

host, port = LOCALHOST_NAME,PORT_ADDRESS
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('/home/mykmyk/servingSockets/keys/Demo.pem', '/home/mykmyk/servingSockets/keys/Demo.key', password="mike")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as my_socket:
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    my_socket.bind((LOCALHOST_NAME, PORT_ADDRESS))
    my_socket.listen(REQUEST_QUEUE_SIZE)
    
    print ("I am listening on :", PORT_ADDRESS)
    
    with context.wrap_socket(my_socket, server_side=True) as serverSock:
        while True:
            try:
                connection, address = serverSock.accept()
                
            except IOError as e:
                code,msg = e.args
                #restart 'accept' if was interrupted
                if code == errno.EINTR:
                    continue
                else:
                    raise        
                    
            pid = os.fork()
            if pid == 0:  #child
                my_socket.close()
                handle_request(connection)
                connection.close()
                os.exit(0)
            else: # parent
                connection.close()   #close parent copy and loop over        
