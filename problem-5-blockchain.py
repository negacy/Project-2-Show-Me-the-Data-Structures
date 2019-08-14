import hashlib
import time

class Block:

    def __init__(self, data, previous_hash):
        #self.timestamp = timestamp
        self.timestamp = time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime())
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(self.data)
        self.next = None
        self.prev = None

    def calc_hash(self, hash_str):
        sha = hashlib.sha256()

        hash_str = hash_str.encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, data):
        if type(data) != str:
            print('Warnning: data should be string.')
            return
        if self.head is None:
            self.head = Block(data, 0)
            self.tail = self.head
            return

        self.tail.next = Block(data, self.tail.hash)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        return
    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += '|'+cur_head.timestamp + ',' + str(cur_head.data) + ',' +cur_head.hash +',' + str(cur_head.previous_hash) + '|'+  " <- "
            cur_head = cur_head.next
        return out_string
    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        
        return size


# Test 1
b1 = DoublyLinkedList() 
b1.append('my first blockchain')
b1.append('second blockchain')
b1.append('third blockchain')
b1.append('forth blockchain')
print(b1)

# Test 2: empty blocks
b2 = DoublyLinkedList()
try:
    b2.append() #raise error when trying to create a block with no data
except TypeError:
   print("Data is a required input to the block")

# Test 3: intput data has to be integer type
b3 = DoublyLinkedList()
b3.append(1)
    
