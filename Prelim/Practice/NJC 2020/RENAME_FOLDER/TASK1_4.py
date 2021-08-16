import socket

s = socket.socket()
s.connect(('127.0.0.1', 1337))
while True:
    data = b''
    while b'\n' not in data:
        data += s.recv(1)
    data = data.decode('utf-8').strip('\n')
    if data[0] == '^':
        print(data[1:])
    elif data[0] == '&':
        print(data[1:], end='')
    elif data[0] == '#':
        raw_input = input('Guess letter:')
        s.send(raw_input.encode())
        s.send(b'\n')
    elif data[0] == '$':
        print(data[1:])
        break
    else:
        print('Invalid CMD received from server')
s.close()
