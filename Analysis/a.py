import random
import time
class AVLTreeNode:
    def __init__(self,key):
        self.key=key
        self.parent=None
        self.left=None
        self.right=None

class AVLTree:
    def __init__(self):
        self.root=None
    
    def height(self,rootNode):
        if rootNode is None:
            return 0
        
        lh=self.height(rootNode.left)
        rh=self.height(rootNode.right)
        
        if lh>rh:
            return lh+1
        else:
            return rh+1

    def search(self,x):
        temp1=self.root
        while temp1!=None:
            if temp1.key>x:
                temp1=temp1.left
            elif temp1.key==x:
                return temp1
            else:
                temp1=temp1.right
        return temp1
    
    def insert(self,key):
        newNode=AVLTreeNode(key)
        #BST INSERT
        temp=self.root
        if temp is None:
            self.root=newNode
            return
        while temp is not None:
            par=temp 
            if temp.key<key:
                temp=temp.right
            else:
                temp=temp.left
            
        if key<par.key:
            par.left=newNode
        else:
            par.right=newNode
        newNode.parent=par
        
      
        
        
        #checking for imbalance
        temp=newNode
        while temp is not None:
            temp=temp.parent
            if temp is None:
                break
            if self.height(temp.left)==self.height(temp.right)+2:
                z=temp
                y=temp.left
                if self.height(y.left)>self.height(y.right):
                    x=y.left
                    #rotating right
                    temp=y.right
                    if z.parent is not None:
                        y.parent=z.parent
                        if z.parent.right is z:
                            z.parent.right=y 
                        else:
                            z.parent.left=y
                    else:
                        y.parent=None
                        self.root=y 
                    y.right=z
                    z.parent=y
                    z.left=temp
                    if temp is not None:
                        temp.parent=z
                else:
                    x=y.right
                    #rotation 1 -- rotating x and y 
                    temp=x.left
                    x.parent=z
                    z.left=x  
                    x.left=y
                    y.parent=x 
                    y.right=temp
                    if temp is not None:
                        temp.parent=y 
                    
                    #rotation 2 -- rotating right 
                    temp=x.right 
                    if z.parent is not None:
                        x.parent=z.parent
                        if z.parent.left is z:
                            z.parent.left=x 
                        else:
                            z.parent.right=x  
                    else:
                        x.parent=None
                        self.root=x 
                    x.right=z 
                    z.parent=x 
                    z.left=temp 
                    if temp is not None:
                        temp.parent=z 
                    
            elif self.height(temp.right)==self.height(temp.left)+2:
                z=temp
                y=temp.right
                if self.height(y.right)>self.height(y.left):
                    x=y.right
                    #rotating left 
                    temp=y.left
                    if z.parent is not None:
                        y.parent=z.parent 
                        if z.parent.right is z:
                            z.parent.right=y 
                        else:
                            z.parent.left=y
                    else:
                        y.parent=None
                        self.root=y 
                    y.left=z 
                    z.parent=y 
                    z.right=temp 
                    if temp is not None:
                        temp.parent=z 
                else:
                    x=y.left
                    #rotation 1 -- rotating x and y 
                    temp=x.right 
                    x.parent=z 
                    z.right=x 
                    x.right=y 
                    y.parent=x 
                    y.left=temp 
                    if temp is not None:
                        temp.parent=y 
                    
                    #rotation 2 -- rotating left 
                    temp=x.left
                    if z.parent is not None:
                        x.parent=z.parent 
                        if z.parent.right is z:
                            z.parent.right=x
                        else:
                            z.parent.left=x 
                    else:
                        x.parent=None
                        self.root=x
                    x.left=z 
                    z.parent=x 
                    z.right=temp 
                    if temp is not None:
                        temp.parent=z 
        
        
    def minimum(self):
        temp=self.root
        while temp.left!=None:
            temp=temp.left
        return temp


    def maximum(self):
        temp=self.root
        while temp.right!=None:
            temp=temp.right
        return temp

    

    def predecessor(self,keyptr):
        temp=keyptr
        if temp.left is not None:
            temp=temp.left
            while temp.right is not None:
                temp=temp.right
            return temp
        while temp.parent is not None:
            if temp.parent.key<keyptr.key:
                return temp.parent
            temp=temp.parent
        return None    

    def successor(self,keyptr):
        temp=keyptr
        if temp.right is not None:
            temp=temp.right
            while temp.left is not None:
                temp=temp.left
            return temp
        while temp.parent is not None:
            if temp.parent.key>keyptr.key:
                return temp.parent
            temp=temp.parent
        return None    
    
    def delete(self,key):
        #searching for key
        keyptr=self.root
        f=-1
        while keyptr is not None:
            if keyptr.key==key:
                f=0
                break
            elif keyptr.key<key:
                keyptr=keyptr.right
            else:
                keyptr=keyptr.left
        if f==-1:
            print("This key doesn't exist in tree.")
            return
        #case 1 - delete leaf
        if keyptr.left is None and keyptr.right is None:
            if keyptr.parent.left is keyptr:
                keyptr.parent.left=None
            else:
                keyptr.parent.right=None
            
        #case 2 - delete node with one child
        elif keyptr.left is None and keyptr.right is not None:
            keyptr.key=keyptr.right.key
            keyptr.right=None
        elif keyptr.left is not None and keyptr.right is None:
            keyptr.key=keyptr.left.key 
            keyptr.left=None 
            
        #case 3 - delete internal node
        else:
            s=self.successor(keyptr)
            keyptr.key=s.key 
            self.delete(s)
            
        #rebalancing the tree
        temp=keyptr 
        while temp is not None:
            temp=temp.parent
            if temp is None:
                break
            if self.height(temp.left)==self.height(temp.right)+2:
                z=temp
                y=temp.left
                if self.height(y.left)>self.height(y.right):
                    x=y.left
                    #save original height of z
                    hz=self.height(z)
                    #rotating right
                    temp=y.right
                    if z.parent is not None:
                        y.parent=z.parent
                        if z.parent.right is z:
                            z.parent.right=y 
                        else:
                            z.parent.left=y
                    else:
                        y.parent=None
                        self.root=y 
                    y.right=z
                    z.parent=y
                    z.left=temp
                    if temp is not None:
                        temp.parent=z
                    
                    #new height of y
                    hy=self.height(y)
                    if hy!=hz:
                        temp=y 
                        continue
                    
                else:
                    x=y.right
                    #rotation 1 -- rotating x and y 
                    temp=x.left
                    x.parent=z
                    z.left=x  
                    x.left=y
                    y.parent=x 
                    y.right=temp
                    if temp is not None:
                        temp.parent=y 
                    
                    #rotation 2 -- rotating right 
                    temp=x.right 
                    if z.parent is not None:
                        x.parent=z.parent
                        if z.parent.left is z:
                            z.parent.left=x 
                        else:
                            z.parent.right=x  
                    else:
                        x.parent=None
                        self.root=x 
                    x.right=z 
                    z.parent=x 
                    z.left=temp 
                    if temp is not None:
                        temp.parent=z 
                    
                    temp=x
                    continue
                    
                    
            elif self.height(temp.right)==self.height(temp.left)+2:
                z=temp
                y=temp.right
                if self.height(y.right)>self.height(y.left):
                    x=y.right
                    hz=self.height(z)
                    #rotating left 
                    temp=y.left
                    if z.parent is not None:
                        y.parent=z.parent 
                        if z.parent.right is z:
                            z.parent.right=y 
                        else:
                            z.parent.left=y
                    else:
                        y.parent=None
                        self.root=y 
                    y.left=z 
                    z.parent=y 
                    z.right=temp 
                    if temp is not None:
                        temp.parent=z
                    
                    hy=self.height(y)
                    if hy!=hz:
                        temp=y
                        continue  
                else:
                    x=y.left
                    #rotation 1 -- rotating x and y 
                    temp=x.right 
                    x.parent=z 
                    z.right=x 
                    x.right=y 
                    y.parent=x 
                    y.left=temp 
                    if temp is not None:
                        temp.parent=y 
                    
                    #rotation 2 -- rotating left 
                    temp=x.left
                    if z.parent is not None:
                        x.parent=z.parent 
                        if z.parent.right is z:
                            z.parent.right=x
                        else:
                            z.parent.left=x 
                    else:
                        x.parent=None
                        self.root=x
                    x.left=z 
                    z.parent=x 
                    z.right=temp 
                    if temp is not None:
                        temp.parent=z 
                    temp=x
                    continue
      
                 
                
            
    
    def preOrderTraversal(self,rootNode):
        temp=rootNode
        if temp is not None:
            print(temp.key,end=' ')
            self.preOrderTraversal(temp.left)
            self.preOrderTraversal(temp.right)
    
    def inOrderTraversal(self,rootNode):
        temp=rootNode
        if temp is not None:
            self.inOrderTraversal(temp.left)
            print(temp.key,end=' ')
            self.inOrderTraversal(temp.right)
    
    def postOrderTraversal(self,rootNode):
        temp=rootNode
        if temp is not None:
            self.postOrderTraversal(temp.left)
            self.postOrderTraversal(temp.right)
            print(temp.key,end=' ')
    

def main():
    tree=AVLTree()
    t1=time.time()
    f=open("Input.lst","r")
    k=0
    for i in range(10):            #npu = [int(i) for i in line.split()]
        tree.insert(int(f.readline()))
        print(int(f.readline()))
        k=k+1
        print(k)
        print("Node inserted")
        
    
    
    t2=time.time()
    tree.preOrderTraversal(tree.root)
    print()
    print()
    print("Time of insertion is")
    print(t2-t1)
    print()
    #t3=time.time()
    # print(tree.search(677994561363370).key)
    #t4=time.time()
    #print("Time for Search is",t4-t3)
    '''tree.insert(25)
    tree.inOrderTraversal(tree.root)
    print()
    tree.preOrderTraversal(tree.root)
    print()
    tree.insert(12)
    tree.inOrderTraversal(tree.root)
    print()
    tree.preOrderTraversal(tree.root)
    print()
    tree.insert(15)
    tree.inOrderTraversal(tree.root)
    print()
    tree.preOrderTraversal(tree.root)
    print()
    tree.insert(20)
    tree.inOrderTraversal(tree.root)
    print()
    tree.preOrderTraversal(tree.root)
    print()
    tree.insert(19)
    tree.inOrderTraversal(tree.root)
    print()
    tree.preOrderTraversal(tree.root)
    print()    
    tree.postOrderTraversal(tree.root)
    print()
    print()
    print()
    print(tree.maximum().key)
    print(tree.minimum().key)
    print(tree.successor(tree.root).key)
    print(tree.predecessor(tree.root).key)
    tree.delete(19)
    tree.inOrderTraversal(tree.root)
    print()
    tree.preOrderTraversal(tree.root)
    print()    
    tree.postOrderTraversal(tree.root)'''
       

if __name__ == '__main__':
    main()