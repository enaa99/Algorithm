import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

class Node:
    def __init__(self,data:int) :
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self) :
        self.root = None
    def push(self,node):
        if self.root == None:
            self.root = node
        else:
            tmp = self.root
            while True:
                if tmp.data < node.data:
                    if tmp.right == None:
                        tmp.right = node
                        break
                    tmp = tmp.right
                else:
                    if tmp.left == None:
                        tmp.left = node
                        break
                    tmp = tmp.left
                
def search(node:Node):
    if node.left != None:
        search(node.left)
    if node.right != None:
        search(node.right)
    print(node.data)


t = Tree()

while True:
    try:
        n = (input())
        t.push(Node(int(n)))
    except :break


search(t.root)

