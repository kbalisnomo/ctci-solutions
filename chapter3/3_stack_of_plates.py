class SetOfStacks:
    def __init__(self, capacity) -> None:
        self.stacks = [[]]
        self.capacity = capacity

    def push(self, value):
        if len(self.stacks[-1]) > self.capacity:
            self.stacks.append([].append(value))
        else:
            self.stacks[-1].append(value)

    def pop(self):
        value = self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:
            self.stacks[-1].pop()
        return value
    
    def popAt(self, index):
        value = self.stacks[index].pop()
        if len(self.stacks[-1]) == 0:
            self.stacks[-1].pop()
        return value