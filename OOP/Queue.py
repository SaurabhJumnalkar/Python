class Queue:
    def __init__(self) -> None:
        self.array=[]
    
    def Enqueue(self,data):
        self.array.append(data)
    
    def Dequeue(self):
        self.array.pop(0)
    
    def Traverse(self):
         for i in range(len(self.array)):
            print(self.array[i] )
    
Q=Queue()
Q.Enqueue(10)
Q.Enqueue(20)
Q.Enqueue(30)
Q.Enqueue(40)
Q.Traverse()
Q.Dequeue()
Q.Dequeue()
Q.Dequeue()
Q.Traverse()