# Node
class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None


# Singly Linked List
class SinglyLinkedList(object):
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
    
    
    def print(self):
        curn = self.head
        string =""
        while curn:
            string += str(curn.data)
            if curn.next:
                string += "->"
            curn = curn.next
        print(string)

if __name__ =="__main__":
    s = SinglyLinkedList()
    #원소 추가
    s.enqueue(Node(1))
    s.enqueue(Node(2))
    s.enqueue(Node(3))
    s.enqueue(Node(4))
    s.enqueue(Node(10))
    s.enqueue(Node(20))
    s.print() # 1->2->3->4->10->20
    
    #원소 삭제
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
    s.print()