class Node:
  def __init__(self,item):
   self.left=None
   self.right=None
   self.val=item

  def  TraversepreOrder(self):
    print(self.val, end=" ")
    if self.left:
      self.left.TraversepreOrder()
    if self.right:
      self.right.TraversepreOrder()
    
    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        print(self.val, end=' ')
        if self.right:
            self.right.traverseInOrder()

  
    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.val, end=' ')


root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)

print("Pre order Traversal: ", end="")
root.traversePreOrder()
print("\nIn order Traversal: ", end="")
root.traverseInOrder()
print("\nPost order Traversal: ", end="")
root.traversePostOrder()

      
    
