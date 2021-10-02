def generateKey(password, message):
    scaled_password = (password * ((len(message) // len(password)) + 1))[:len(message)]
    return scaled_password

def encrypt(password, message):
    secret_key = generateKey(password, message)
    encrypted_msg = [chr(ord(i)+ord(j)) for i,j in zip(message, secret_key)]
    return ''.join(encrypted_msg)

print(generateKey('cat', 'hello'))

def decrypt(password, message):
    secret_key = generateKey(password, message)
    decrypted_msg = [chr(ord(i)-ord(j)) for i,j in zip(message, secret_key)]
    return ''.join(decrypted_msg)

print(decrypt("cat", encrypt("cat","hello")))

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

q = Queue(10)
q.enqueue('A')
q.enqueue('B')
q.enqueue('C')
print(q.array)
q.display()

print(q.dequeue())