class Solution:
    def __init__(self):
        self.stack = []
        self.queue = []
        
    def pushCharacter(self,ch):
        self.stack.append(ch)
        
    def enqueueCharacter(self,ch):
        self.queue.append(ch)
        
    def popCharacter(self):
        return self.stack.pop()
    
    def dequeueCharacter(self):
        ch = self.queue[0]
        self.queue.remove(ch)
        return ch
