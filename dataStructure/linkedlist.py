#Node 클래스 정의
class Node:
    def __init__(self, data) :
        self.data = data
        self.next = None
        
        
#LinkedList 클래스 (자료구조) 정의
class LinkedList:
    #초기화 메서드
    def __init__(self) :
        self.head = None
        self.tail = None
        
    def push_back(self,node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
    def push_front(self,node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        