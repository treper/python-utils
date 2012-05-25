import socket
class MockServant(host,port):
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host='127.0.0.1'