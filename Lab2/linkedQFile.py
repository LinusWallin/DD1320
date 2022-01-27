
class Node:
  """
  Attributes:
    :int: value: the value of the current spot in the linked list.
    :int: next: the "arrow" pointing to the next value in the linked list.
  """
  def __init__(self, value, next = None):
    """
    Assigns default attributes to the node.
    :int: value: the value of the current node value.
    :int: next: the "arrow" pointing to the next node value in the linked list.
    """
    self.value = value
    self.next = next

class LinkedQ:
  """
  Queues and dequeues nodes from a linked list. Also keeps track of the first and last element of the linked list.
  :obj: first: the object of the first spot in the linked list.
  :obj: last: the object pointing to the last node value in the linked list.
  """
  def __init__(self, first = None, last = None):
    """
    Assign default attributes.
    :obj: first: the object of the first spot in the linked list.
    :obj: last: the object pointing to the last node value in the linked list.
    """
    self._first = first
    self._last = last

  def isEmpty(self):
    """
    Check if the linked list is empty.
    :return: returns a boolean
    """
    if self._first == None:
      return True
    else:
      return False
  
  def enqueue(self, x):
    """
    Queues nodes in the linked list. First checks if the linked list is empty, if not, then link the new node to the end of the linked list. Otherwise, add the node to the linked list.
    :str: x: a string value to be added to the linked list.
    """
    node = Node(x)
    if self.isEmpty():
      self._first = node
      self._last = node
    else:
      self._last.next = node
      self._last = self._last.next
  
  def dequeue(self):
    """
    Dequeues nodes from the linked list (the first value of the linked list).
    :return: the value of the node removed from the list.
    """
    tmp_first = self._first
    self._first = self._first.next
    return tmp_first.value

