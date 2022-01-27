class Node:
  """
  Attributes:
    :obj: left: The left child of the node
    :obj: right: The right child of the node
    :str: value: The value of the node
  """
  def __init__(self, value):
    """
    Assigns values to the attributes
    """
    self.left = None
    self.right = None
    self.value = value

class Bintree:
  """
  Attributes:
    :obj: root: The root node
  """
  def __init__(self):
    """
    Sets the root node to None
    """
    self.root = None
  
  def put(self, new_value):
    """
    Assigns a new node to the binary search tree and assigns it as the 
    root if there is no root.
    :str: new_value: A string with the value to put in the binary tree
    """
    if self.root is None:
      self.root = Node(new_value)
    else:
      putta(self.root, new_value)

  def __contains__(self, value):
    """Checks if the value exists in the binary search tree.
    :str: value: The string to check for
    """
    return finns(self.root, value)
    
  def write(self):
    """
    Prints out the binary tree in inorder.
    """
    skriv(self.root)
    print("\n")


def putta(node, new_value):
  #"Problem solving with algortihms and data structures using python"
  #Chapter 7.13
  #https://runestone.academy/runestone/books/published/pythonds/Trees/SearchTreeImplementation.html
  """
  Function adds nodes to the binary search tree based on some constrains and recursively. If the value to be added is larger than of the current node node, keep stepping to the right. If it is smaller than the current node value, keep stepping to the left and so on.
  :obj: node: the current node in the binary search tree hierarchy.
  :str: new_value: the value to be added to the new node in the search tree.
  """
  if new_value < node.value:
    if node.left is not None:
      putta(node.left, new_value)
    else:
      node.left = Node(new_value)
  else:
    if node.right is not None:
      putta(node.right, new_value)
    else:
      node.right = Node(new_value)

def finns(root, value):
  """
  Function checks if a value already exists in the binary search tree recursively.
  :obj: root: the rood node of the binary search tree.
  :str: the value that is looked for in the binary search tree.
  :return: boolean value stating whether or not the value was found in the binary search tree.
  """
  #Function from lecture 4 
  #https://canvas.kth.se/courses/26987/pages/forelasning-4-binara-trad
  if root == None:
    return False
  if value == root.value:
    return True
  if value < root.value:
    return finns(root.left, value)
  if value > root.value:
    return finns(root.right, value)
    
def skriv(node):
  """Prints out the binary tree from the node in inorder.
  :obj: node: the node of which the value should be printed.
  """
  #Function from lecture 4 
  #https://canvas.kth.se/courses/26987/pages/forelasning-4-binara-trad
  if node != None:
    skriv(node.left)
    print(node.value)
    skriv(node.right)