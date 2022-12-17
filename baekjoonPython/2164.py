import sys

input = sys.stdin.readline


n = int(input())

# 한장 버리고 한장 뒤로

class Node(object):
    def __init__(self,data) :
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self) :
        self.head = None
        self.tail = None
    
    #Add new node at the end of the linked list
    def enqueue(self,node):
        if self.head == None:
            self.head = node
            self.tail = node
        else :
            self.tail.next =node
            self.tail = self.tail.next
    def dequeue(self):
        if self.head == None:
            return -1
        
        v= self.head.data
        self.head = self.head.next
        
        if self.head == None:
            self.tail = None
        return v
    def front(self):
        if self.head == None:
            return -1
        v = self.head.data
        return v

q = LinkedList()
for i in range(1,n+1):
    q.enqueue(Node(i))

for i in range(n-1):
    q.dequeue()
    tmp = q.dequeue()
    q.enqueue(Node(tmp))

print(q.dequeue())