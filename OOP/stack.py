
class Stack:
    def __init__(self):
        self.array = []

    def push(self):
        self.array.append(int(input()))

    def pop(self):
        self.array.pop()

    def traverse(self):
        for i in range(len(self.array)):
            print(self.array[i],end=" " )

    def tos(self):
        print(self.array[len(self.array)-1])


S = Stack()
S.push()
S.push()
S.traverse()
S.push()
S.push()
S.traverse()
S.pop()
S.traverse()
S.tos()
