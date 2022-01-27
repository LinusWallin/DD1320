from array import array

class ArrayQ:
  """
  Attributes:
    :list: data: a list with data to be added to a queue.
  """
  def __init__(self, data = ""):
    """
    Creates an array with the data provided.
    :list: data: a list with data to be added to a queue.
    """
    self._arr = array('u', data)

  def __str__(self):
    """
    Prints the array as a string.
    :return: returns the array as a string
    """
    out_str = ''
    for i in range(len(self._arr)):
      out_str += str(self._arr[i])
    return out_str
    
  def isEmpty(self):
    """
    Checks if the array is empty
    :return: returns a boolean
    """
    if self._arr.buffer_info()[1] == 0:
      return True
    else:
      return False

  def enqueue(self, nr):
    """
    Adds an element to the end of the queue.
    :str: nr: the element to add to the queue
    :returns: returns a string
    """
    self._arr.append(str(nr))
    return 'Success.\n'
    
  def dequeue(self):
    """
    Takes out the first element of the array.
    :return: returns the first element of the array
    """
    return self._arr.pop(0)