import datetime
import math
from hashlib import sha256
import time


# from block import Block
# from blockchain import Blockchain
from random import random, sample


def take_from_user():
    attacker_power = input("Enter the attacker's computational power in percentage: ")
    return attacker_power


def action():
    number_of_block = 10
    num = float(take_from_user()) / 100
    attacker_per = num
    honest_per = (1 - attacker_per)

    num1 = math.floor(number_of_block * attacker_per)
    for block in range(num1):
        list1 = ["seif eldeen ", "seif adel", "seif emad", "hayat", "hussein", "hamza", "emad", "thoraya", "ahmed",
                 "toka", "bahgat", "amr"]

        random_transaction = {"sender": (sample(list1, 1)), "receiver": (sample(list1, 1)), "amount": 10000* random()}

        attacker_blockchain.add_block(random_transaction)

    num2 = math.floor(number_of_block * honest_per)
    for block in range(num2):
        list1 = ["seif eldeen ", "seif adel", "seif emad", "hayat", "hussein", "hamza", "emad", "thoraya", "ahmed",
                 "toka", "bahgat", "amr"]

        random_transaction = {"sender": (sample(list1, 1)), "receiver": (sample(list1, 1)), "amount":10000* random()}

        local_blockchain.add_block(random_transaction)

    if attacker_per >= 0.51:
        print("attacker succedded")

    else:
        print("attacker failed")


class Block:
    def __init__(self, transactions, previous_hash):
        self.time_stamp = datetime.datetime.now()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.generate_hash()

    def generate_hash(self):
        block_header = str(self.time_stamp) + str(self.transactions) + str(self.previous_hash) + str(self.nonce)
        block_hash = sha256(block_header.encode())
        return block_hash.hexdigest()

    def print_contents(self):
        print("timestamp:", self.time_stamp)
        print("transactions:", self.transactions)
        print("current hash:", self.generate_hash())
        print("previous hash:", self.previous_hash)
        print("nonce: ", self.nonce)

    def proof_of_work(self, difficulty=2):
        self.hash = self.generate_hash()
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.generate_hash()
        # block.nonce = 0
        return self.hash


class Blockchain:
    def __init__(self):
        self.chain = []
        self.unconfirmed_transactions = []
        self.genesis_block()

    def genesis_block(self):
        transactions = []
        genesis_block = Block(transactions, "0")
        genesis_block.generate_hash()
        self.chain.append(genesis_block)

    def add_block(self, transactions):
        previous_hash = (self.chain[len(self.chain) - 1]).hash
        new_block = Block(transactions, previous_hash)
        # new_block.generate_hash()
        proof = new_block.proof_of_work()
        self.chain.append(new_block)
        # return proof

    def print_blocks(self):
        for i in range(len(self.chain)):
            current_block = self.chain[i]
            print("Block {} {}".format(i, current_block))
            current_block.print_contents()

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if (current.hash != current.generate_hash()):
                print("Current hash does not equal generated hash")
                return False
            if (current.previous_hash != previous.generate_hash()):
                print("Previous block's hash got changed")
                return False
        return True

    def find_hardness(self):
        N = 1
        t1 = time.time()
        local_blockchain.chain[2].proof_of_work(N)

        t2 = time.time()
        T = t2 - t1
        print("time:")
        print(T)
        while not (T < 1.1 and T > 1):
            if T < 0.4:
                N = N + 1
            else:
                N = N - 1
            t1 = time.time()
            local_blockchain.chain[2].proof_of_work(N)

            t2 = time.time()
            T = t2 - t1
            print("time:")
            print(T)
        print(N)
        return N

def user_choices():
    print("to show the honest user chain enter 0")
    print("to show the attacker chain enter 1")
    choice=input("to show both enter 2\n")
    if int(choice)==0:
        local_blockchain.print_blocks()
        choice2=input('do you want to view difficulty simulation y/n:')
        if choice2=='y':
            local_blockchain.find_hardness()

        else:
            pass

    elif int(choice)==1:
        attacker_blockchain.print_blocks()
        choice2=input('do you want to view difficulty simulation y/n:')
        if choice2=="y":

            local_blockchain.find_hardness()
        else:
            pass
    elif int(choice)==2:
        print("attacker blockchain")
        attacker_blockchain.print_blocks()
        print("__________")
        print("honest user blockchain")
        local_blockchain.print_blocks()
        choice2=input('do you want to view difficulty simulation y/n:')
        if choice2=="y":
            pass
            local_blockchain.find_hardness()
        else:
            pass



block_one_transactions = {"sender": "Alice", "receiver": "Bob", "amount": "50"}
block_two_transactions = {"sender": "Bob", "receiver": "Cole", "amount": "25"}
block_three_transactions = {"sender": "Alice", "receiver": "Cole", "amount": "35"}



attacker_blockchain = Blockchain()
local_blockchain = Blockchain()
# local_blockchain.print_blocks()

local_blockchain.add_block(block_one_transactions)
local_blockchain.add_block(block_two_transactions)
local_blockchain.add_block(block_three_transactions)

attacker_blockchain.add_block(block_one_transactions)
attacker_blockchain.add_block(block_two_transactions)
attacker_blockchain.add_block(block_three_transactions)
#local_blockchain.find_hardness()
action()
#print("---------------")
#local_blockchain.print_blocks()
#print("---------------")
#attacker_blockchain.print_blocks()

# N=input("Enter N(number of zeros): ")

user_choices()
# local_blockchain.chain[2].transactions = fake_transactions

# local_blockchain.validate_chain()
# attacker_blockchain.validate_chain()
