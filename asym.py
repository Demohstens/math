import threading

class Asym():
    def __init__(self, obj : iter) -> None:
        self.left_stack = []  # Even indecies go here
        self.right_stack = [] # Odd indecies go here
        # distribute the iters over both stacks 
        for i, n in enumerate(obj):
            if i % 2 == 0:
                self.left_stack.append(n)
            else:
                self.right_stack.append(n)

        self.longer = self.left_stack if len(self.left_stack) > len(self.right_stack) else self.right_stack

    def __str__(self) -> str:
        index = 0
        ret = ""
        while True:
            try:
                ret += self.left_stack[index]
            except IndexError:
                return ret
            try:
                ret += self.right_stack[index] 
                index += 1
            except IndexError:
                return ret
            if index == len(self.longer):
                break
        return ret
    
    def __iter__(self):
        return self