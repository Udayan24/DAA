# 41117 - Udayan Chavan - P1
# Write a program to implement Huffman Encoding using a greedy strategy.

# Priority Queue Implementation
import heapq

# Huffman Tree Node
class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.f = freq
        self.s = symbol

        self.l = left
        self.r = right

        self.huff = "" # 0/1

    def __lt__(self, nxt):
        return self.f < nxt.f

# Recursive function to display nodes and their frequencies
def printNodes(node, val=""):
    newVal = val + str(node.huff)

    if node.l:
        printNodes(node.l, newVal)
    if node.r:
        printNodes(node.r, newVal)

    if not node.l and not node.r:
        print(node.s,":",newVal)

# ----------------------------------------------
# ----------- TEST CASE 1 ------------
'''chars = ["a", "b", "c", "d", "e", "f"]
freq = [5, 9, 12, 13, 16, 45]'''

# ----------- TEST CASE 2 ------------
'''chars = ["a", "b", "c", "d", "e"]
freq = [3, 7, 6, 5, 9]'''

# ----------- TEST CASE 3 ------------
chars = ["a", "b", "c", "d", "e", "f"]
freq = [50, 10, 30, 5, 3, 2]
# ----------------------------------------------

# A heap for storing nodes
nodes = []

# Create Nodes and push them to the nodes heap 
for x in range(len(chars)):
    n = Node(freq[x], chars[x])
    heapq.heappush(nodes, n)

# Arrive at a single root node
while len(nodes) > 1:
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)

    left.huff = 0
    right.huff = 1

    n = Node(left.f + right.f, left.s + right.s, left, right)

    heapq.heappush(nodes, n)

# --------- Output ---------
print("\nCharacters:", chars)
print("Frequencies:", freq)
print("\nEncoded values:")
printNodes(nodes[0])