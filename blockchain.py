from hashlib import sha256

class Block:
    def __init__(self, message):
        self.message = message
        self.messageHash = sha256(message.encode()).hexdigest()

    def getHash(self):
        header = self.previousBlockHash + self.messageHash + hex(self.difficulty)[2:].rjust(2, '0') + hex(self.nonce)[2:].rjust(8, '0')
        return sha256(sha256(header.encode()).digest()).hexdigest()

class Blockchain:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.target = '0'*difficulty
        genesis = Block('genesis')
        genesis.blockId = 0
        genesis.previousBlockHash = 'coffee78'*8
        genesis.difficulty = 0
        genesis.nonce = 88
        genesis.blockHash = genesis.getHash()
        self.chain = [genesis]

    def add(self, block):
        block.blockId = len(self.chain)
        block.previousBlockHash = self.chain[-1].blockHash
        block.difficulty = self.difficulty
        for nonce in range(2**32):
            block.nonce = nonce
            blockHash = block.getHash()
            if blockHash.startswith(self.target):
                block.blockHash = blockHash
                self.chain.append(block)
                return True
        return False

bc = Blockchain(3)
bc.add(Block('hello world'))
bc.add(Block('you can trust me'))

for b in bc.chain:
    print(b.message)
    print(b.messageHash)
    print(b.previousBlockHash)
    print(b.nonce)
    print(b.blockHash)
    print('~'*40)
