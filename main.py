import hashlib
import json
from time import time

def __init__(self):
    """Initialize blockchain"""
    self.chain = []
    self.current_transactions = []
    self.new_block(previous_hash=1, proof=100)

def proof_of_work(self, last_proof):
   """Issuing proof of work"""
   proof = 0
   while self.valid_proof(last_proof, proof) is False:
       proof +=1
   return proof

@staticmethod
def valid_proof(last_proof, proof):
   """Validate block"""
   guess = f'{last_proof}{proof}'.encode()
   guess_hash = hashlib.sha256(guess).hexigest()
   return guess_hash[:4] == "0000"

def new_block(self, proof, previous_hash = None):
    """Create new blocks and then add them to existing chain"""
    block = {
       'index': len(self.chain) + 1,
       'timestamp' : time(),
       'proof': proof,
       previous_hash: previous_hash or self.hash(self.chain[-1]),
    }
    self.current_transactions = []
    self.chain.append(block)
    return block


def new_transaction(self):
    """Add a new transaction to already existing transactions"""
    self.current_transactions.append({
        'sender': sender,
        'recipient': recipient,
        'amount': amount,
    })
    return self.last_block['index'] + 1

@staticmethod
def hash(block):
    """Hash function for blocks"""
    block_string = json.dumps(block, sort_keys = True).encode()
    return hashlib.sha256(block_string).hexdigest()

@property
def last_block(self):
    """Return the last block of the chain"""
    return self.chain[-1]
