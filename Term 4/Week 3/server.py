import socket as sc
def generateKey(password, message):
    scaled_password = (password * ((len(message) // len(password)) + 1))[:len(message)]
    return scaled_password

def encrypt(password, message):
    secret_key = generateKey(password, message)
    encrypted_msg = [chr(ord(i)+ord(j)) for i,j in zip(message, secret_key)]
    return ''.join(encrypted_msg)

def decrypt(password, message):
    secret_key = generateKey(password, message)
    decrypted_msg = [chr(ord(i)-ord(j)) for i,j in zip(message, secret_key)]
    return ''.join(decrypted_msg)

class Queue:
    def __init__(self, n) -> None:
        self.items = 0
        self.tail = 0
        self.head = -1
        self.size = n
        self.array = [None for _ in range(self.size)]

    def isFull(self):
        return self.head == self.tail
    
    def isEmpty(self):
        return self.head == -1
    
    def enqueue(self, string):
        if not self.isFull():
            self.array[self.tail] = string
            self.tail = (self.tail + 1) % self.size
            if self.head == -1:
                self.head += 1
            self.items += 1
            return ""
        else:
            return "Queue is full!"
    
    def dequeue(self):
        if not self.isEmpty():
            ret = self.array[self.head]
            self.array[self.head] = None
            self.head = (self.head + 1) % self.size
            if self.head == self.tail:
                self.head = -1
                self.tail = 0
            self.items -= 1
            return ret
        else:
            return "Queue is empty!"
    
    def display(self):
        if not self.isEmpty():
            h = self.head
            while h != self.tail:
                print(self.array[h])
                h = (h + 1) % self.size
            return
        else:
            print('Queue is empty!')
            return

    def current_size(self):
        return self.items

q = Queue(266)

menu = \
"""
1) Wait for connection from client for next pickup request
2) Dequeue
"""

password = input('Please set a password:\nAnswer: ')

while True:
    print('Next action?')
    print(menu)
    option = int(input('Type an option: '))

    if option == 1:
        with sc.socket() as ls:
            ls.bind(('localhost', 9999))
            ls.listen()
            print('Awaiting connection from pickup client')
            s, addr = ls.accept()
            print('Connection established!')
            print('Receiving data from client')
            data = b''
            while b'\n' not in data:
                data += s.recv(1)
            data = data.decode().strip().split('/')
            data = [decrypt(password,i) for i in data]
            print('Checking client\'s secret key')
            if data[0] == password:
                print('Client\'s secret key is correct!')
                print(f'Client\'s Team name: {data[2]}')
                print(f'Group size: {data[1]}')
                print(f'No. of passengers in queue: {q.current_size()}')
                if q.current_size() + int(data[1]) < q.size:
                    print('You have capacity for them.')
                    pickup = True if input('Confirm Pickup? Y/N') == 'Y' else False
                    if pickup == True:
                        s.send(encrypt(password, 'confirmed').encode())
                        q.enqueue(data[2])
                        print('Added to queue. Items in queue now are:')
                        q.display()
                    else:
                        s.send(encrypt(password, 'cancelled').encode())
                else:
                    print('You do not have capacity for them.')
            else:
                print('Client\'s secret key is incorrect!')
        print('Connection disconnected.')

    elif option == 2:
        size_dequeue = int(input('How many to dequeue? '))
        for i in range(size_dequeue):
            print(q.dequeue())

