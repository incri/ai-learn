class PPjQueue:
    
    def __init__(self):
        self.queue = []
    
    def isEmpty(self):
        if len(self.queue) <= 0:
            return True
        else:
            return False
    
    def enqueue(self, element):
        self.queue.append(element)
    
    def dequeue(self):
        element = self.queue[0:1]  
        del self.queue[0]
        return  element