import socket


def getSecret():
    words = {}
    words_raw = []
    with open('WORDS.txt') as f:
        for line in f:
            words_raw.append(line.strip())

    for word in words_raw:
        if len(word) in words.keys():
            words[len(word)].append(word.lower())
        else:
            words[len(word)] = [word]
    shortest_word = min(words.keys())
    longest_word = max(words.keys())
    import random
    return random.sample(words[random.randint(shortest_word, longest_word)], 1)[0].lower()


def mask(word: str, guessed_char):
    return ''.join([i if i in guessed_char else '.' for i in word])


with socket.socket() as ls:
    ls.bind(('127.0.0.1', 1337))
    ls.listen()
    print('LISTENING ...')
    while True:
        s, addr = ls.accept()
        print(f'ACCEPTED {addr}')
        import random
        import math
        word = getSecret()
        print(word)
        guesses = len(word) * 2
        guessed_char = random.sample(word, math.ceil(0.2*len(word)))
        s.send(f'^You have {guesses} attempts. Good Luck!\n'.encode())
        s.send(b'^'+mask(word, guessed_char).encode()+b'\n')
        for attempt in range(guesses, 0, -1):
            s.send(f'&[{attempt}]\n'.encode())
            s.send(b'#\n')
            data = b''
            while b'\n' not in data:
                data += s.recv(1)
            guess = str(data.decode()).strip('\n').lower()
            if guess in word:
                guessed_char.append(guess)
            s.send(b'^'+mask(word, guessed_char).encode()+b'\n')
            if '.' not in mask(word, guessed_char):
                s.send(b'$WIN\n')
                break
        else:
            s.send(f'$LOSE ... The word is {word}\n'.encode())
            break
