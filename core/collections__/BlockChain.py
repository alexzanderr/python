

import json
from hashlib import sha256
from collections import OrderedDict


class Block:
    def __init__(self, name, index, previous_hash=None):
        self.name = name
        self.index = index
        self.previous_hash = previous_hash
        self.current_hash = sha256(json.dumps(self.__dict__, indent=4).encode()).hexdigest()


    def __str__(self):
        return json.dumps({
            "name": self.name,
            "index": self.index,
            "prev_hash": self.previous_hash,
            "current_hash": self.current_hash
        }, indent=4)


if __name__ == '__main__':
    first_block = Block("first", 0)
    second_block = Block("second", 1, first_block.current_hash)
    third_block = Block("third", 2, second_block.current_hash)
    print(first_block, second_block, third_block, sep="\n")