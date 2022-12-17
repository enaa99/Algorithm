import sys

input = sys.stdin.readline

N = int(input())

class Node:
    def __init__(self,data,left,right) :
        self.data = data
        self.left = left
        self.right = right

tree ={}


for _ in range(N):
    a,b,c = map(str,input().split())
    
    tree[a] = Node(a,b,c)


def post_order(node:Node):
    
    if node.left != '.':
        post_order(tree[node.left])
    if node.right != '.':
        post_order(tree[node.right])
    print(node.data, end='')

def pre_order(node:Node):
    print(node.data, end='')
    if node.left != '.':
        pre_order(tree[node.left])
    if node.right != '.':
        pre_order(tree[node.right])

def in_order(node:Node):
    if node.left != '.':
        in_order(tree[node.left])
        
    print(node.data, end='')
    if node.right != '.':
        in_order(tree[node.right])


pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])