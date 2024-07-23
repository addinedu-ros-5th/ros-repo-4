import socket

class ESP32Master:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def send_signal(self, signal_message):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.ip, self.port))
                s.sendall(signal_message.encode() + b'\n')
                response = s.recv(1024)
                print(f'Received from ESP32: {response.decode()}')
        except socket.error as e:
            print(f'Error sending signal: {e}')


    def close(self):
        self.sock.close()

        
