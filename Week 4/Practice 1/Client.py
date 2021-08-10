import socket

s = socket.socket()
s.connect(('127.0.0.1', 1337))
while True:
    data = b''
    while b'$' not in data:
        data += s.recv(1)
    data = data.decode('utf-8').strip('$')
    if data[0] == '^':
        print(data[1:])
    elif data[0] == '%':
        raw_input = input('YOUR MOVE [X/Y]> ')
        s.sendall(raw_input.encode('utf-8'))
        s.sendall(b'$')
    elif data[0] == '*':
        print('TERMINATING... ')
        break
    else:
        print('Invalid CMD received from server')
s.close()
