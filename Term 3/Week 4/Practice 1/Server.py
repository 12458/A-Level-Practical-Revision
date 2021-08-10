import socket


class TicTacToe:
    def __init__(self):
        self.board = [[0 for _ in range(3)] for _ in range(3)]

    def render(self):
        header = ' 012\n'
        board_str = '\n'.join([''.join([str(y) for y in x])
                              for x in self.board])
        board_str = board_str.replace('0', '-')
        board_str = board_str.replace('1', 'X')
        board_str = board_str.replace('2', 'O')
        tmp = board_str.split('\n')
        for i in range(len(tmp)):
            tmp[i] = str(i) + tmp[i]
        return header + '\n'.join(tmp)

    def make_move(self, player, x, y):
        if self.is_valid_move(x, y):
            self.board[y][x] = player

    def is_valid_move(self, x, y):
        return True if 0 <= x <= 2 and 0 <= y <= 2 and self.board[y][x] == 0 else False

    def game_end(self):
        tictactoe_lut = \
            [
                [
                    [1, 0, 0],
                    [1, 0, 0],
                    [1, 0, 0]],
                [
                    [0, 1, 0],
                    [0, 1, 0],
                    [0, 1, 0]
                ],
                [
                    [0, 0, 1],
                    [0, 0, 1],
                    [0, 0, 1]
                ],
                [
                    [1, 1, 1],
                    [0, 0, 0],
                    [0, 0, 0]
                ],
                [
                    [0, 0, 0],
                    [1, 1, 1],
                    [0, 0, 0]
                ],
                [
                    [0, 0, 0],
                    [0, 0, 0],
                    [1, 1, 1]
                ],
                [
                    [1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1]
                ],
                [
                    [0, 0, 1],
                    [0, 1, 0],
                    [1, 0, 0]
                ]
            ]

        def isolate(player: str):
            if player == 'O':
                tmp = [[1 if j == 2 else 0 for j in i] for i in self.board]

            else:
                tmp = [[1 if j == 1 else 0 for j in i] for i in self.board]
            tmp2 = []
            import numpy
            for i in tictactoe_lut:
                tmp2.append(numpy.bitwise_and(
                    numpy.array(tmp), numpy.array(i)).tolist())
            return tmp2

        for i in isolate('X'):
            if i in tictactoe_lut:
                return (True, 'X')
        for i in isolate('O'):
            if i in tictactoe_lut:
                return (True, 'O')
        if all([0 not in x for x in self.board]):
            return (True, None)
        else:
            return (False, None)


ls = socket.socket()
ls.bind(('127.0.0.1', 1337))
ls.listen()
print('LISTENING')
while True:
    s, addr = ls.accept()
    print(f'ACCEPTED {addr}')
    t = TicTacToe()
    while True:
        for cur_player in [1, 2]:
            print(t.render())
            s.sendto(b'^', addr)  # Demarcate print
            s.sendto(t.render().encode('utf-8'), addr)
            s.sendto(b'$', addr)  # Demarcate end
            if cur_player == 1:
                s.sendto(b'%', addr)  # Demarcate print
                s.sendto(b'$', addr)  # Demarcate end
                data = b''
                while b'$' not in data:
                    data += s.recv(1)
                x, y = data.decode('utf-8').strip('$').split('/')
                x, y = int(x), int(y)
                t.make_move(cur_player, x, y)
            else:
                x, y = input('YOUR MOVE [X/Y]> ').strip().split('/')
                x, y = int(x), int(y)
                t.make_move(cur_player, x, y)
            end = t.game_end()
            # print(end)
            if end[0] and end[1] != None:
                s.sendto(b'^', addr)  # Demarcate print
                string = f'Player {end[1]} wins'
                s.sendto(string.encode('utf-8'), addr)
                s.sendto(b'$', addr)  # Demarcate end
                s.sendto(b'^', addr)  # Demarcate print
                s.sendto(t.render().encode('utf-8'), addr)
                s.sendto(b'$', addr)  # Demarcate end
                s.sendto(b'*$', addr)  # Demarcate termination
                print(string)
                break
            elif end[0] and end[1] == None:
                s.sendto(b'^', addr)  # Demarcate print
                s.sendto(b'TIE', addr)
                s.sendto(b'$', addr)  # Demarcate end
                s.sendto(b'^', addr)  # Demarcate print
                s.sendto(t.render().encode('utf-8'), addr)
                s.sendto(b'$', addr)  # Demarcate end
                s.sendto(b'*$', addr)  # Demarcate termination
                print('TIE')
                break
        else:
            continue
        break

s.close()
