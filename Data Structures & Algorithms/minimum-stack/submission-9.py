class MinStack:    

    def __init__(self):
        self.elements = []
        self.minEls = []
        

    def push(self, val: int) -> None:
        self.elements.append(val)
        if len(self.elements) == 1 or val <= self.minEls[-1]:
            self.minEls.append(val)

    def pop(self) -> None:
        val = self.elements.pop()
        if val == self.minEls[-1]:
            self.minEls.pop()
        

    def top(self) -> int:
        return self.elements[-1]
        
    def getMin(self) -> int:
        return self.minEls[-1]
        
