string = 'BCAADDDCCACACAC' 

class NodeTree(object): 
    def __init__(self, left=None, right=None): 
        self.left = left 
        self.right = right 

    def children(self): 
        return (self.left, self.right) 

    def nodes(self): 
        return (self.left, self.right) 

    def __str__(self): 
        return '%s_%s' % (self.left, self.right) 

def huffman_code_tree(node, left=True, binString=''): 
    if type(node) is str: 
        return {node: binString} 
    (l, r) = node.children() 
    d = dict() 
    d.update(huffman_code_tree(l, True, binString + '0')) 
    d.update(huffman_code_tree(r, False, binString + '1')) 
    return d 

freq = {} 
for c in string: 
    if c in freq: 
        freq[c] += 1 
    else: 
        freq[c] = 1 

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True) 

nodes = freq 

while len(nodes) > 1: 
    (key1, c1) = nodes[-1] 
    (key2, c2) = nodes[-2] 
    nodes = nodes[:-2] 
    node = NodeTree(key1, key2) 
    nodes.append((node, c1 + c2))
    nodes = sorted(nodes, key=lambda x: x[1], reverse=True) 

huffmanCode = huffman_code_tree(nodes[0][0]) 

print(' Char | Huffman code ') 
print('----------------------') 
for (char, frequency) in freq: 
    print(' %-4r |%12s' % (char, huffmanCode[char]))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     🌳 THEORY BEHIND THE CODE — Huffman Coding

# Goal: Compress data by assigning shorter binary codes to more frequent characters and longer codes to less frequent ones.

# Core Idea:

# Calculate the frequency of each character.

# Build a binary tree (Huffman Tree) — lower-frequency characters go deeper, higher-frequency ones stay near the root.

# Traverse the tree — left edge = 0, right edge = 1.
# The binary path from root → leaf = Huffman code for that character.

# Replace each character with its code → compressed bitstream.

# Why it works:
# It’s an example of an optimal prefix code — no code is a prefix of another, so decoding is unambiguous.

# Used concepts:

# Greedy Algorithm: Always combine the two lowest-frequency nodes first.

# Binary Trees

# Recursion

# Dictionary sorting with lambda

# Object-Oriented Programming (class NodeTree)

# 🧠 LINE-BY-LINE EXPLANATION
# Input String
# string = 'BCAADDDCCACACAC'


# This is the message to encode.
# Characters: A, B, C, D appear multiple times.

# NodeTree class
# class NodeTree(object): 
#     def __init__(self, left=None, right=None): 
#         self.left = left 
#         self.right = right 


# Defines a binary tree node.
# Each node has:

# left child (0 path)

# right child (1 path)

# These will later be characters or subtrees.

#     def children(self): 
#         return (self.left, self.right) 


# Returns both children as a tuple — used to traverse easily.

#     def nodes(self): 
#         return (self.left, self.right) 


# Duplicate of children(). (Could be merged; redundancy is fine here for clarity.)

#     def __str__(self): 
#         return '%s_%s' % (self.left, self.right)


# Defines how the node prints itself (string representation).
# For example, if left = A and right = B → prints "A_B".

# Recursive Huffman Tree Traversal
# def huffman_code_tree(node, left=True, binString=''):


# Recursive function that traverses the Huffman tree to assign binary codes.

# node: current node in tree

# left: whether we came from a left branch

# binString: the current binary path (starts empty, adds ‘0’ or ‘1’ at each step)

#     if type(node) is str: 
#         return {node: binString} 


# Base case: if the node is just a character (leaf), return {char: code}.

#     (l, r) = node.children() 
#     d = dict() 
#     d.update(huffman_code_tree(l, True, binString + '0')) 
#     d.update(huffman_code_tree(r, False, binString + '1')) 
#     return d 


# Recursive case:

# Visit left child, add '0'

# Visit right child, add '1'

# Merge both dictionaries into one

# This returns {char: binary_code} for every character.

# Frequency Calculation
# freq = {} 
# for c in string: 
#     if c in freq: 
#         freq[c] += 1 
#     else: 
#         freq[c] = 1 


# Count frequency of each character.
# Result for 'BCAADDDCCACACAC' →
# {'B':1, 'C':5, 'A':5, 'D':3}

# Sort by frequency
# freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)


# Convert dict → list of tuples → sort descending by count.
# Result: [('C',5), ('A',5), ('D',3), ('B',1)]

# Build Huffman Tree
# nodes = freq 


# Initial list of (symbol, frequency) pairs.

# while len(nodes) > 1: 
#     (key1, c1) = nodes[-1] 
#     (key2, c2) = nodes[-2] 


# Takes the two least frequent nodes (end of sorted list).

#     nodes = nodes[:-2] 
#     node = NodeTree(key1, key2) 
#     nodes.append((node, c1 + c2))


# Remove them

# Create a new internal node combining them

# Append it back with combined frequency

#     nodes = sorted(nodes, key=lambda x: x[1], reverse=True) 


# Re-sort so smallest frequencies stay at end.
# Loop continues until only one root node remains.

# Generate Huffman Codes
# huffmanCode = huffman_code_tree(nodes[0][0])


# Starts recursive traversal from the root node → generates a code dictionary.
# Example output might be:
# {'C': '0', 'A': '10', 'D': '110', 'B': '111'}

# Print Results
# print(' Char | Huffman code ') 
# print('----------------------') 
# for (char, frequency) in freq: 
#     print(' %-4r |%12s' % (char, huffmanCode[char]))


# Nicely formats the character and its binary Huffman code.

# 🔁 DRY RUN EXAMPLE

# For 'BCAADDDCCACACAC':

# Char	Frequency	Huffman Code
# C	5	0
# A	5	10
# D	3	110
# B	1	111

# Encoded string:
# 'BCAADDDCCACACAC' → 1110 10 10 110110110 00 10 0 10 0 10 0
# Compression achieved — average bits per symbol reduced.

# ⚙️ EXPECTED EXAM MODIFICATIONS

# Here are the most likely changes they might ask you to implement:

# Print frequency table before coding

# for k, v in freq:
#     print(f"{k}: {v}")


# Decode a given encoded string

# Traverse the Huffman tree using bits until you reach a character node.

# Reset at root for next symbol.

# Accept user input
# Replace the hardcoded string with input("Enter a string: ").

# Show total bits before & after compression

# original_bits = len(string) * 8
# compressed_bits = sum(len(huffmanCode[ch]) * string.count(ch) for ch in huffmanCode)
# print(f"Compression ratio: {compressed_bits/original_bits:.2f}")


# Handle single character edge case
# If input = 'AAAAA', Huffman code should assign '0' to it.

# Add visualization (optional)
# Print tree in pre-order traversal or show pairs merged at each step.

# 🎓 VIVA QUESTIONS (and crisp answers)

# Q1. What is Huffman coding used for?
# Data compression — reducing file size by using shorter codes for frequent characters.

# Q2. What kind of algorithm is Huffman coding?
# A greedy algorithm — it builds the optimal prefix code step by step by choosing locally optimal pairs.

# Q3. Why is Huffman coding optimal?
# Because it always combines the two least frequent symbols, ensuring minimal average code length (proved by Huffman in 1952).

# Q4. What is a prefix code?
# No code is a prefix of another, enabling unambiguous decoding.

# Q5. Why recursion?
# The tree structure is naturally recursive: each subtree is itself a smaller Huffman tree.

# Q6. Time complexity?
# Building: O(n log n) (because of repeated sorting)
# Encoding lookup: O(1) average (using dictionary)

# Q7. What happens if two characters have equal frequency?
# Their order can vary, but overall compression efficiency remains the same.

# Q8. What data structures are used?
# Dictionaries, tuples, lists, and a binary tree.

# 💡 BONUS KNOWLEDGE

# Huffman coding is used in JPEG, MP3, ZIP, PNG.

# Modern compressors use adaptive Huffman or arithmetic coding for better efficiency.

# Can be extended to handle symbol pairs or variable alphabets.

# If you share your next code, I’ll format the explanation in exactly this structure — theory → line-by-line → dry run → modifications → viva → extras — so you can memorize both the logic and the examiner traps.
