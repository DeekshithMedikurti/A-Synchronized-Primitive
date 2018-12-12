import socket
import os, os.path
class centralized:
    
    #initialize server
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setblocking(True)
        self.sock.bind((self.host, self.port))
    
    def listen(self):
        while True:
            self.sock.listen(1)
            conn, addr = self.sock.accept()
            try:
                lock = False
                data = conn.recv(1024)
                if not data:
                    break
                var = str(data.decode('utf8'))
                print('var:',var)
                if var == 'lock'and lock != True:
                    conn.send('ok'.encode('utf8'))
                    lock = True
                    if not os.path.exists('/Users/deekshithbucky/PycharmProjects/Project2/lock.txt'):
                        with open('/Users/deekshithbucky/PycharmProjects/Project2/lock.txt','x') as f:
                            f.write(str(0))
                    else:
                        with open('/Users/deekshithbucky/PycharmProjects/Project2/lock.txt', 'r+') as f:
                            data = int(f.read())
                            f.write(str(data+1))
                        lock = False
                else:
                    conn.send('wait'.encode('utf8'))
            except:
                conn.close()

if __name__ == "__main__":
    server = centralized("localhost",6889)
    server.listen()