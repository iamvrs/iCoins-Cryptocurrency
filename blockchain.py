import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

def calculate_hash(index, previous_hash, timestamp, data):
    value = str(index) + str(previous_hash) + str(timestamp) + str(data)
    return hashlib.sha256(value.encode()).hexdigest()

def create_genesis_block():
    return Block(0, "0", time.time(), "Genesis Block", calculate_hash(0, "0", time.time(), "Genesis Block"))

def create_new_block(previous_block, data):
    index = previous_block.index + 1
    timestamp = time.time()
    hash = calculate_hash(index, previous_block.hash, timestamp, data)
    return Block(index, previous_block.hash, timestamp, data, hash)

# Example usage:
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# Add new blocks
block1 = create_new_block(previous_block, "Transaction Data 1")
blockchain.append(block1)
previous_block = block1

block2 = create_new_block(previous_block, "Transaction Data 2")
blockchain.append(block2)

# Display blockchain
for block in blockchain:
    print(f"Index: {block.index}, Hash: {block.hash}")
