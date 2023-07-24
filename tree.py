class Node:
  def __init__(self,item):
    self.left=None
    self.right=None
    self.val=item
  def postorder(root):
    if root:
      print(str(root.val) + '->' , end= " ")
      postorder(root.left)
      postorder(root.right)
   def inorder(root):
     if root:
       inorder(root.left)
       print(str(root.val) + '->' , end =" ")
       inorder(root.right)
  def postorder(root):
    if root:
      postorder(root.left)
      postorder(root.right)
      print(str(root.val) + '->' , end =" ")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder traversal ")
inorder(root)

print("\nPreorder traversal ")
preorder(root)

print("\nPostorder traversal ")
postorder(root)
