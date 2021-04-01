class Node:
    def __init__(self,Data):
        self.next= None
        self.Data=Data

class LinkedList:
    def __init__(self) :
        self.Head=None
    def CreateAtStart(self,newData):
        p=Node(newData)
        if self.Head==None:
            self.Head=p
        else:
            self.next=self.Head
            self.Head=p    

    def CreateAtEnd(self,newData):
        p=Node(newData)
        if self.Head==None:
            self.Head=p
        else:
            temp=self.Head
            while temp.next:
                temp=temp.next
            temp.next=p


    def DeleteAtStart(self):
        if self.Head==None:
            print("Empty Linked List")
        else:
            p=self.Head
            self.Head=self.Head.next
            del p
        
    def CreateAtGivenLOcation(self,loc,newData):
        p=Node(newData)
        if self.Head==None and loc==1:
            self.Head=p
        else: 
            i=1
            count=0
            q=self.Head
            while i<loc-1 and q !=None:
                q=q.next
                i=i+1
            if q==None:
                print("Invalid Location")
            else:
                p.next=q.next
                q.next=p
            

    def DeleteAtEnd(self):
        pass
    def DeleteAtGivenLocation(self):
        pass