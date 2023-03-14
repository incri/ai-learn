class PPjStack:
    
    def __init__(self):
        self.stack = []
    
    def isEmpty(self):
        if len(self.stack) <= 0:
            return True
        else:
            return False
    
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        return self.stack.pop()   