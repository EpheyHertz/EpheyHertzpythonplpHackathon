class QueueWithStacks:
    def __init__(self) :
        self.stack1=[]
        self.stack2=[]

    def enqueue(self,y:int):
       self.stack1.append(y)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            raise IndexError("Dequeueing from an empty queue")
        return self.stack2.pop()
    

q = QueueWithStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())
print(q.dequeue())

        