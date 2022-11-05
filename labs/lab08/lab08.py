from typing import List, Optional
import random

class RandomChoiceIterator:
    def __init__(self, values: List[int], num_iters: Optional[int] = None):
        self.values = values
        self.num_iters = num_iters
        self.current_num_iters = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num_iters != None:
            if self.current_num_iters >= self.num_iters:
                raise StopIteration()

            self.current_num_iters += 1

            return random.choice(self.values)
        else:
            return random.choice(self.values)


for value in RandomChoiceIterator([1, 2, 3], num_iters=5):
    print(value)

ORIGINAL_HEIGHT = 120
DELICACIES = ["bottle", "cake", "one side of the mushroom", "other side of the mushroom"]

current_height = ORIGINAL_HEIGHT / 5

for find in RandomChoiceIterator(DELICACIES):
    if find == "bottle":
        current_height = current_height / 5
    elif find == "cake":
        current_height = current_height * 2.5
    elif find.startswith("one side"):
        current_height = current_height / 2.5
    else:
        assert find.startswith("other side")

        current_height = current_height * 5

    if current_height == ORIGINAL_HEIGHT:
        print("Alice's Adventure is over! ...Next one is on its way?")

        break
    else:
        print(
            f"Alice found {find} and her current height is {current_height} != {ORIGINAL_HEIGHT}."
            f" So Alice continues her adventures in Wonderland..."
        )