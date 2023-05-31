#import library
import heapq

#create class
class node:
    #constructor_1
    def __init__(self, freq, symbol, left=None, right=None):

        #frequency
        self.freq = freq

        #symbol
        self.symbol = symbol

        #left node of current tree
        self.left = left

        #right node of current tree
        self.right = right

        #blank string
        self.huff = ''

    #constructor 2
    def __lt__(self, nxt):
        return self.freq < nxt.freq

def printNodes(node, val=''):
    
    #create newVal
    newVal = val + str(node.huff)

    #if node --> not an edge node --> traverse inside
    if(node.left):
        printNodes(node.left, newVal)
    if(node.right):
        printNodes(node.right, newVal)

    #if node --> edge node --> display huffman node
    if(not node.left and not node.right):
        print(f"{node.symbol} -> {newVal}")

#character list
chars = ['a', 'b', 'c', 'd', 'e', 'f']

#frequency list
freq = [5, 9, 12, 13, 16, 45]

#empty list
nodes = []

#pushing values in nodes
for x in range(len(chars)):
    heapq.heappush(nodes, node(freq[x], chars[x]))

while len(nodes)>1:

    #sort them in ascending order - Nodes
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)

    #direction assigning
    left.huff = 0
    right.huff = 1

    #combine 2 smallest nodes and make parent node
    newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)

    #push it into the heapq library
    heapq.heappush(nodes, newNode)

#disply huffman tree
printNodes(nodes[0])






