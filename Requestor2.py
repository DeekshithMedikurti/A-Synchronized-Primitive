import socket
import time

HOST = "localhost"
PORT = 6889
class Requestor2:
    
    def main(self):
        #create a socket and connect to the server
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((HOST,PORT))
        try:
            attempt = 0
            while(attempt < 3):
                s.send('lock'.encode('utf8'))
                data = s.recv(1024)
                msg = data.decode('utf8')
                if msg == 'wait':
                      time.sleep(.300)  
                      attempt += 1
                else:
                    print('Process-2 Acquired the lock and finished.')
                    s.close()
        except:
            s.close()

if __name__ == "__main__":
    req = Requestor2()
    req.main()