import time

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=Node(0)

    
    def PrintList(self):
        if self.head.next is None:
            print("List is empty")
            return
        temp=self.head.next
        while temp is not None:
            print(temp.value,end=' ')
            temp=temp.next
        print(" ")


    def Insert(self,val,posNode):
        newNode=Node(val)

        #empty list
        if self.head.next is None:
            self.head.next=newNode
            #print("List after insertion is: ",end=' ')
            #self.PrintList()
            return
        
        else:
            temp=posNode.next
            posNode.next=newNode
            newNode.next=temp
            #print("List after insertion is: ",end=' ')
            #self.PrintList()
            return

    
    def InsertAtIndex(self,val,pos):
        if pos<0:
            print("Invalid position")
            return
        newNode=Node(val)
        #empty list
        if self.head.next is None:
            self.head.next=newNode
            #print("List after insertion is: ",end=' ')
            #self.PrintList()
            return
        #insert at head
        if pos == 0:
            temp=self.head.next
            self.head.next=newNode
            newNode.next=temp
            #print("List after insertion is: ",end=' ')
            #self.PrintList()
        else:
            current=self.head.next
            posCounter=0
            while current is not None:
                if posCounter == pos:
                    temp=current.next
                    current.next=newNode
                    newNode.next=temp
                    #print("List after insertion is: ",end=' ')
                    #self.PrintList()
                    return
                current=current.next
                posCounter+=1
            
            print("Position out of bounds!")
        

    
    def DeleteNode(self,key):
        current=self.head.next
        pos=None
        while current.next is not None:
            if current.next.value == key:
                pos=current
            current=current.next
        #pos=self.Search(pos)
        #print(pos.next.value)
        #Empty list
        if pos:
            if self.head.next is None:
                print("List is empty, can't delete!")
                return
        
            if pos.next is not None:
                pos.next=pos.next.next
                return
            #print("List after deletion is: ",end=' ')
            #self.PrintList()
            #return
        
        print("Position out of bounds")


    def Search(self,val):
        current=self.head.next
        while current is not None:
            if current.value == val:
                return current
            current=current.next
        return None


    def Length(self):
        current=self.head.next
        len=0
        while current is not None:
            len+=1
            current=current.next
        return len


    def IsEmpty(self):
        if self.head.next is None:
            return True
        else:
            return False


def main():
    '''L = LinkedList()
    L.Insert(10,L.head)
    L.Insert(12,L.head.next)
    L.Insert(2,L.head)
    print('Size of L is ',L.Length())
    L.DeleteNode(L.head)
    L.DeleteNode(L.head.next)
    print('List is empty?',L.IsEmpty())
    print('Size of L is ',L.Length())
    L.DeleteNode(L.head)
    print('List is empty?',L.IsEmpty())
    print('Size of L is ',L.Length())
    L.InsertAtIndex(2,0)
    L.InsertAtIndex(1,0)
    L.InsertAtIndex(4,2)
    L.InsertAtIndex(3,2)'''
    r=int(input("Enter the range"))
    L = LinkedList()
    f = open("input.lst","r")
    t1=time.clock()
    for i in range(r):
        L.Insert(int(f.readline()),L.head)
    t2=time.clock()
    print("Insert time: ",t2-t1)
    print()
    t1=time.clock()
    L.Search(1)
    t2=time.clock()
    print("Search time: ",t2-t1)
    print()
    t1=time.clock()
    L.DeleteNode(1)
    t2=time.clock()
    print("Delete time: ",t2-t1)

if __name__ == '__main__':
    main()
