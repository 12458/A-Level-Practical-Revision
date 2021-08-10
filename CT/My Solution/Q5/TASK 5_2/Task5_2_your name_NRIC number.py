import socket

listen_socket = socket.socket()
listen_socket.bind(('127.0.0.1', 9999))
listen_socket.listen()

s, addr = listen_socket.accept()
data=b''
while b'\n' not in data:
        data += s.recv(1024)
data=data.decode('utf-8').strip()

data=data.split(',')
lut_h2={'A': 20,
        'B': 17.5,
        'C': 15,
        'D': 12.5,
        'E': 10,
        'S': 5,
        'U': 0
            }
lut_h1 = {'A': 10,
        'B': 8.75,
        'C': 7.5,
        'D': 6.25,
        'E': 5,
        'S': 2.5,
        'U': 0
        }
# 10(GP) + 10(PW) + 60(3H2) + 10(1H1) = 90.
igp = lut_h1[data[0].strip()] + lut_h1[data[1].strip()] + lut_h2[data[2].strip()] \
+ lut_h2[data[3].strip()] + lut_h2[data[4].strip()] + lut_h1[data[5].strip()]

s.sendall(f"{igp}".encode('utf-8'))

s.close()

listen_socket.close()
