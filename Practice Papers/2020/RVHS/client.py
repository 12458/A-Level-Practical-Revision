import socket

menu = \
"""
Menu:
1) Guess a letter
2) Guess a word
3) Quit
"""

s = socket.socket()
s.connect(('localhost', 12345))

while True:
    data = b''
    while b'\n' not in data:
        data += s.recv(1)
    rx_msg_str = data.decode().strip()
    if rx_msg_str[:5] == "START":
        length_word = int(rx_msg_str[6:])
        word = ['?' for _ in range(length_word)]
        print(''.join(word))
    elif rx_msg_str[:5] == "GUESS":
        if len(rx_msg_str) == 5:
            pass
        else:
            locations_update = rx_msg_str[6:].split(',')
            for location in locations_update:
                word[int(location)] = letter
            print(''.join(word))
            # update str
    elif rx_msg_str[:3] == "WIN":
        print('WIN!')
        raise SystemExit
    elif rx_msg_str[:3] == "LOSE":
        print('LOSE')
        raise SystemExit
    else:
        print('ERROR')
        raise Exception('Unexpected message')
    print(menu)
    try:
        option = int(input('OPTION> ').strip())
        assert 1 <= option <= 3
    except:
        print('Invalid option selected')
        continue

    if option == 1:
        letter = input('GUESS LETTER> ').strip()
        s.send(f'GUESS,{letter}\n'.encode())
    elif option == 2:
        word = input('GUESS WORD> ').strip()
        s.send(f'HWORD,{word}\n'.encode())
    else:
        print('You quit!')
        s.send(f'QUIT\n'.encode())
        break