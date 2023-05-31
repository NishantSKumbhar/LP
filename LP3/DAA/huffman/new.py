import heapq

class node:
    def __init__(self, freq, symbol, left=None, right=None):

        self.freq = freq

        self.symbol = symbol

        self.left = left

        self.right = right

        self.huff = ''

    def __lt__(self, nxt):
        return self.freq < nxt.freq

def printNodes(node, val=''):
    # pass

    #create newVal
    newVal = val + str(node.huff)

    #if node --> not an edge node --> traverse there
    if node.left:
        printNodes(node.left, newVal)
    if node.right:
        printNodes(node.right, newVal)

    #if node --> edge node --> print
    if(not node.left and not node.right):
        print(f"{node.symbol} -> {newVal}")

chars = ['a', 'b', 'c', 'd', 'e', 'f']

freq = [5, 9, 12, 13, 16, 45]

nodes = []

for x in range(len(chars)):
    heapq.heappush(nodes, node(freq[x], chars[x]))

while len(nodes)>1:

    #sort
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)

    #direction
    left.huff = 0
    right.huff = 1

    #combine smallest nodes and make parent node
    newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)

    #push it into library
    heapq.heappush(nodes, newNode)

#display huffman tree - print the function
printNodes(nodes[0])
